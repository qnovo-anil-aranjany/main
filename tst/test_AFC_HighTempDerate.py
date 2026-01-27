"""Test Module Description:
    Test module for HSD time-based testing.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.12.4
    - Pytest version >= 8.0.1
"""
import math

from .main import *
from .main import _MODULE_PATH

ffi = cffi.FFI()
SKIP_TEST = False
MAKE_HTML = True
if not SKIP_TEST:
    _FILENAME = "high_temp_derate_data.xlsx"

    def parse_AFC_high_temp_derate_data():
        file_path = join(dirname(_MODULE_PATH), "test_data", _FILENAME)
        logger.info(file_path)
        test_cases = []
        soc = 0
        for row in iter_file(file_path):
            for key, value in row.items():
                temp = float(key)
                ratio = float(value)
                if math.isclose(ratio, 1.0, abs_tol=1e-6):
                    ratio = 1
                output = ratio * 10000
                test_case = {
                    "Inputs": {
                        "soc": soc,
                        "temp": temp,
                        "ratio": ratio,
                        "output": output,
                    },
                    "Expected": {},
                }
                test_cases.append(test_case)
            soc += 5
        return test_cases

    all_time_steps = parse_AFC_high_temp_derate_data()

    @pytest.mark.parametrize("test_cases", all_time_steps)
    @allure.feature(
        """
            JIRA-ID: QAFC-443, QAFC-108, QAFC-93, QAFC-94, QAFC-95

            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge. ,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_HiTemperatureDerate from afc binary via cffi.,\
            Step4: compare output with expected value from input param - VeAFC_I_ChgPackCurr,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: qnovo_afc_features.c
            Method_In_Test: AFC_HiTemperatureDerate

            parent_suite: swc_fast_charge
            suite: afc_high_temperature_derate
            sub_suite: high_temperature_derate
            label: Unit / Integration
        """
    )
    def test_AFC_HighTemp_Derate(lib: Any, setup_parameters, test_cases):
        """
        This test function performs verification of specific operating conditions relevant to the
        'AFC_HiTemperatureDerate' function.
        """

        lib.VeAPI_T_MaxTempSnsr = int(10 * test_cases["Inputs"]["temp"])
        lib.VeAFC_I_ChgPackCurr = 10000
        lib.VeAPI_Pct_PackSOC = int(100 * test_cases["Inputs"]["soc"])
        logger.debug(f"Temp set is: {lib.VeAPI_T_MaxTempSnsr}")
        logger.debug(f"soc set is : {lib.VeAPI_Pct_PackSOC}")
        # Run Function
        # ------------------------------------------------
        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        lib.AFC_HiTemperatureDerate()
        actual = lib.VeAFC_I_ChgPackCurr
        expected = test_cases["Inputs"]["output"]
        logger.info(f"ACTUAL : {actual} ")
        logger.info(f"EXPECTED   : {int(expected)}")
        # To accommodate minor difference between python and c
        if abs(int(expected) - actual) == 1:
            expected = actual

        compare_result(int(expected), actual)
