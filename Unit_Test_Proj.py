import unittest
from GedcomProject import AnalyzeGEDCOM, Family, Individual, CheckForErrors
import datetime
import os

class ProjectTest(unittest.TestCase):
    """Tests that our GEDCOM parser is working properly"""

    def __init__(self, *args, **kwargs):
        super(ProjectTest, self).__init__(*args, **kwargs)
        cwd = os.path.dirname(os.path.abspath(__file__)) #gets directory of the file
        file_name = cwd + "\Bad_GEDCOM_test_data.ged"
        self.all_errors = AnalyzeGEDCOM(file_name, False, False).all_errors #done in this method so it only happens once

    def test_dates_before_curr(self):
        """US01: Unit Test: to ensure that all dates occur before the current date"""
        list_of_known_errors=["US01: The marriage of Future Trunks and Mai Trunks cannot occur after the current date.",
                              "US01: The divorce of Future Trunks and Mai Trunks cannot occur after the current date.",
                              "US01: The birth of Future Trunks cannot occur after the current date.",
                              "US01: The birth of Mai Trunks cannot occur after the current date.",
                              "US01: The death of Future Trunks cannot occur after the current date."]
        for error in list_of_known_errors:
            self.assertIn(error, self.all_errors)

    def test_indi_birth_before_marriage(self):
        """US02: Unit Test: to ensure that birth of an individual occurs before their marriage"""
        list_of_known_errors = ["US02: Johnny /Sway/'s birth can not occur after their date of marriage",
                                "US02: Missy /Kennedy/'s birth can not occur after their date of marriage",
                                "US02: Bobby /Bourne/'s birth can not occur after their date of marriage and Bella /Bourne/'s birth can not occur after their date of marriage" ]
        for error in list_of_known_errors:
            self.assertIn(error, self.all_errors)

    def test_birth_before_death(self):
        """US03: Unit Test: to ensure that birth occurs before the death of an individual"""
        list_of_known_errors = ["US03: James /Nicholas/'s death can not occur before their date of birth",
                                "US03: Peter /Tosh/'s death can not occur before their date of birth"]
        for error in list_of_known_errors:
            self.assertIn(error, self.all_errors)

    def test_marr_before_div(self):
        """US04: Unit Test: to ensure that marriage dates come before divorce dates"""
        list_of_known_errors = [
            "US04: Johnson /Deere/ and Emily /Deere/'s divorce can not occur before their date of marriage"]
        for error in list_of_known_errors:
            self.assertIn(error, self.all_errors)

    def test_marr_div_before_death(self):
        """US05 & US06: Tests that the marr_div_before_death method works properly, the list of known errors is manually hard coded.
        It contains all of the errors we have intentionally put into the file and ensures the file catches them"""
        list_of_known_errors = ["US05 & US06: Either Mark /Eff/ or Jess /Eff/ were married or divorced after they died", "US05 & US06: Either Troy /Johnson/ or Sammy /Johnson/ were married or divorced after they died"]
        for error in list_of_known_errors:
            self.assertIn(error, self.all_errors)

    def test_normal_age(self):
        """US07: Tests that the normal_age method works properly"""
        list_of_known_errors = [
            "US07: John /Old/'s age calculated (1000) is over 150 years old",
            "US07: Jackie /Old/'s age calculated (168) is over 150 years old"]
        for error in list_of_known_errors:
            self.assertIn(error, self.all_errors)

    def test_birth_before_marriage(self):
        """US08: Tests to see if birth_before_marriage function is working properly
            Will raise exceptions if birth is before marriage or 9
            months after the divorce of the parents"""
        #Tests child is born 1 month before parents are married
        list_of_known_errors = [
            "US08: Jimmy /Shmoe/ was born before their parents were married",
            "US08: Sammy /Shmoe/ was born 60 months after their parents were divorced"]
        for error in list_of_known_errors:
            self.assertIn(error, self.all_errors)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
