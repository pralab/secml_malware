import os, glob
from secml.array import CArray
from secml.ml.classifiers import CClassifier
from secml_malware.utils.remote_request import forwardService
from secml_malware.utils.antivirus_service import AntivirusService, MetaDefender, NetAV, VirusTotal
from secml_malware.utils.is_valid_url import isValidUrl
import numpy as np
import json
import io
import hashlib

class CClassifierRemote(CClassifier):
    
    def __init__(self, url:str=None, antivirus:str=None, apiKey:str=None):
        """
        Creates the Remote Classifier.

        Parameters
        ----------
        url : str
                remote server URL
        """
        if not isValidUrl(url):
            raise ValueError("Please, provide a valid URL or container name in the form of "
                             "http://<container_name>:<port>/<route>.")
        super(CClassifierRemote, self).__init__()
        self._url = url
        self._antivirus = antivirus
        self._apiKey = apiKey

        # fix this to bypass _check_is_fitted
        self._classes = np.array([0, 1])
        self._n_features = 2

    def get_apikey(self):
        return self._apiKey

    def get_av(self):
        return self._antivirus

    def get_url(self):
        return self._url

    def _backward(self, w):
        raise NotImplementedError("Backward is not implemented.")

    def _fit(self, x, y):
        raise NotImplementedError("Fit is not implemented.")

    def initializeAV(self):
        # default value if no conditions are met
        obj = None

        if self.get_av() == "virustotal":
            obj = VirusTotal(self._apiKey)

        elif self.get_av() == "metadefender":
            obj = MetaDefender(self._apiKey)

        elif self.get_av() is None:
            obj = NetAV()

        return obj

    def return_verdict(self, response):
        """
        Given the response, it calculates the probability of the examined file being a malware
        as a CArray([malware, goodware])
        :param response:
        :return:
        """
        if self.get_av() == "virustotal":
            score = CArray(response["data"]["attributes"]["stats"]["malicious"])
            scores = score.atleast_2d()
            tot_av = 70 # numero di engines testati TODO not sure about that
            tot_av_detect = [[tot_av / tot_av - c / tot_av, c / tot_av] for c in scores]
            verdict = CArray(tot_av_detect)
            return verdict

        elif self.get_av() == "metadefender":
            score = CArray(response["scan_results"]["total_detected_avs"])
            scores = score.atleast_2d()
            tot_av = 32 # numero di engines testati
            tot_av_detect = [[tot_av/tot_av - c/tot_av, c/tot_av] for c in scores]
            verdict = CArray(tot_av_detect)
            return verdict

        elif self.get_av() is None:
            score = CArray(response)
            scores = score.atleast_2d()
            confidence = [[1 - c, c] for c in scores]
            verdict = CArray(confidence)
            return verdict

    def _forward(self, x):

        x_list = x.tolist()[0]
        x_bytes = b''.join([bytes([i]) for i in x_list])

        # Bytestring conversion to sha256 for identifying the file
        hash_filename = hashlib.sha256(x_bytes)
        hex_hash = hash_filename.hexdigest()

        av = self.initializeAV()
        engine = self.get_av()

        # TODO ; accorpare i due rami ?
        if engine is None:
            response = av.scan_file(x_bytes, self._url, hex_hash)

        elif engine == "virustotal":
            bytes_io = io.BytesIO(x_bytes)
            # Create a BufferedReader object from the BytesIO object
            bufferedFile = io.BufferedReader(bytes_io)
            # Send buffered file
            response = av.scan_file(bufferedFile)

        elif engine == "metadefender":
            response = av.scan_file(x_bytes, self._url, hex_hash)

        return self.return_verdict(response)
