import unittest
from tasks.medical_transcription import (get_medical_speciality_sample_names,
                                         get_medical_specialities_count, 
                                         get_medical_specalities)

class TestMedicalTranscription(unittest.TestCase):
    
    medical_specialities = open('tests/transcription_outputs/get_medical_specalities.txt', 'r').read()
    medical_specialities_count = open('tests/transcription_outputs/get_medical_specialities_count.txt', 'r').read()
    medical_speciality_sample_names = open('tests/transcription_outputs/get_medical_speciality_sample_names.txt', 'r').read()
    
    def test_len_get_medical_specalities(self):
        assert len(str(get_medical_specalities())) == len(self.medical_specialities)
        
    def test_content_get_medical_specalities(self):
        assert str(get_medical_specalities()) == self.medical_specialities
    
    def test_len_get_medical_specialities_count(self):
        assert len(str(get_medical_specialities_count())) == len(self.medical_specialities_count)
        
    def test_content_get_medical_specialities_count(self):
        print(f"{str(get_medical_specialities_count())} -> {self.medical_specialities_count}")
        assert str(get_medical_specialities_count()) == self.medical_specialities_count
        
    def test_len_get_medical_speciality_sample_names(self):
        assert len(str(get_medical_speciality_sample_names())) == len(self.medical_speciality_sample_names)
        
    def test_content_get_medical_speciality_sample_names(self):
        assert str(get_medical_speciality_sample_names()) == self.medical_speciality_sample_names
        
        
if __name__ == "__main__":
    unittest.main()
        

    
        