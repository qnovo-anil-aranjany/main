"""Test Module Description:
    Test module for HSD time-based testing.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""

import ast
import csv
from os.path import abspath, dirname, join
from typing import Any

import cffi
import pytest

from submodules.tool_test_automation.src.common.fixtures import lib
from submodules.tool_test_automation.src.common.utils import (
    iter_file,
    lib_array_to_list,
    validate_with_reference_data,
    write_output_to_excel,
)

ffi = cffi.FFI()
SKIP_TEST = False
MAKE_HTML = True
if not SKIP_TEST:
    _MODULE_PATH = abspath(__file__)
    _SUBDIR_NAME = "time_based_data"
    _FILENAME = "TTIX2086_AFC_MaccorLog_Cycle36_r50300-1004_replicate.csv"

    def parse_AFC_Behavioral_Test_data(file_path):
        test_cases = []
        for row in iter_file(file_path):
            # Get inputs
            test_filename = row["filename"]
            Time = int(row["Time"])
            PackSOC = int(row["PackSOC"])
            PackSOC_DR = int(row["PackSOC_DR"])
            PackCurr = int(row["PackCurr"])
            PackCurr_DR = int(row["PackCurr_DR"])

            try:
                SEVolts = [int(item) for item in ast.literal_eval(row["SEVolts"])]
            except TypeError:
                SEVolts = [int(row["SEVolts"])]

            try:
                SEVolts_DR = [
                    int(item) for item in ast.literal_eval(row["SEVolts_DR"])
                ]
            except TypeError:
                SEVolts_DR = [int(row["SEVolts_DR"])]

            try:
                TempSnsrs = [int(item) for item in ast.literal_eval(row["TempSnsrs"])]
            except TypeError:
                TempSnsrs = [int(row["TempSnsrs"])]

            try:
                TempSnsrs_DR = [
                    int(item) for item in ast.literal_eval(row["TempSnsrs_DR"])
                ]
            except TypeError:
                TempSnsrs_DR = [int(row["TempSnsrs_DR"])]

            MinTempSnsr = int(row["MinTempSnsr"])
            MinTempSnsr_DR = int(row["MinTempSnsr_DR"])

            MaxTempSnsr = int(row["MaxTempSnsr"])
            MaxTempSnsr_DR = int(row["MaxTempSnsr_DR"])

            ChgPackCapcty = int(row["ChgPackCapcty"])
            ChgPackCapcty_DR = int(row["ChgPackCapcty_DR"])

            battery_state = row["battery_state"]
            EVSEChgStatus = int(row["EVSEChgStatus"])

            # Format data for parametrized test
            test_case = {
                "Inputs": {
                    "filename": test_filename,
                    "Time": Time,
                    "PackSOC": PackSOC,
                    "PackSOC_DR": PackSOC_DR,
                    "PackCurr": PackCurr,
                    "PackCurr_DR": PackCurr_DR,
                    "SEVolts": SEVolts,
                    "SEVolts_DR": SEVolts_DR,
                    "TempSnsrs": TempSnsrs,
                    "TempSnsrs_DR": TempSnsrs_DR,
                    "MinTempSnsr": MinTempSnsr,
                    "MinTempSnsr_DR": MinTempSnsr_DR,
                    "MaxTempSnsr": MaxTempSnsr,
                    "MaxTempSnsr_DR": MaxTempSnsr_DR,
                    "ChgPackCapcty": ChgPackCapcty,
                    "ChgPackCapcty_DR": ChgPackCapcty_DR,
                    "battery_state": battery_state,
                    "EVSEChgStatus": EVSEChgStatus,
                },
                "Expected": {},
            }

            test_cases.append(test_case)

        return test_cases

    def test_AFC_Behavioral_replicateMaccorLog(lib: Any):
        _SUBDIR_NAME1 = "time_based_data\\input_data"
        dir_path = join(dirname(_MODULE_PATH), _SUBDIR_NAME1)
        file_path = join(dir_path, _FILENAME)
        all_time_steps = parse_AFC_Behavioral_Test_data(file_path)

        # Initialize results
        results = {
            "filename": [],
            "Time": [],
            "PackCurr": [],
            "PackCurr_DR": [],
            "SEVolts": [],
            "SEVolts_DR": [],
            "TempSnsrs": [],
            "TempSnsrs_DR": [],
            "MinTempSnsr": [],
            "MinTempSnsr_DR": [],
            "MaxTempSnsr": [],
            "MaxTempSnsr_DR": [],
            "ChgPackCapcty": [],
            "ChgPackCapcty_DR": [],
            "PackSOC": [],
            "PackSOC_DR": [],
            "Battery_State": [],
            "EVSEChgStatus": [],
            " ": [],
            "WarningFlags (dec)": [],
            "WarningFlags (bin)": [],
            "ChgPackCurr": [],
            "ChgPackVolt": [],
            "ChgCompletionFlag": [],
            "QnovoAFC_LogVar1\nl_LoggingPath (dec)": [],
            "QnovoAFC_LogVar1\nl_LoggingPath (bin)": [],
            "QnovoAFC_LogVar2\nl_InitializedFlag": [],
            "QnovoAFC_LogVar3\nl_ValidSampleFlag": [],
            "QnovoAFC_LogVar4\nl_QNS_State": [],
            "QnovoAFC_LogVar5\nl_PresentStageNum": [],
            "QnovoAFC_LogVar6\nl_HighestIndex": [],
            "QnovoAFC_LogVar7\nl_CCCPS_Index": [],
            "QnovoAFC_LogVar8\nl_CCCPS_Stage": [],
            "QnovoAFC_LogVar9\nl_CPVCorrIdx": [],
            "QnovoAFC_LogVar10\nl_CV_Curr": [],
            "QnovoAFC_LogVar11\nl_CalcCurrForStage": [],
            "QnovoAFC_LogVar12\nl_PreChgCurr": [],
            "QnovoAFC_LogVar13\nl_PostChgCurr": [],
            "QnovoAFC_LogVar14\nl_Post_Volt": [],
            "QnovoAFC_LogVar15\nl_SampleSEVolt": [],
            "QnovoAFC_LogVar16\nl_RefSEVolt": [],
        }

        for each_time_step in all_time_steps:
            # Setup Variables
            # ------------------------------------------------
            test_filename = each_time_step["Inputs"]["filename"]
            input_time = each_time_step["Inputs"]["Time"]
            lib.VeAPI_I_PackCurr = each_time_step["Inputs"]["PackCurr"]
            lib.VeAPI_b_PackCurr_DR = each_time_step["Inputs"]["PackCurr_DR"]
            lib.VaAPI_U_SEVolts = each_time_step["Inputs"]["SEVolts"]
            lib.VaAPI_b_SEVolts_DR = each_time_step["Inputs"]["SEVolts_DR"]
            lib.VaAPI_T_TempSnsrs = each_time_step["Inputs"]["TempSnsrs"]
            lib.VaAPI_b_TempSnsrs_DR = each_time_step["Inputs"]["TempSnsrs_DR"]
            lib.VeAPI_T_MinTempSnsr = each_time_step["Inputs"]["MinTempSnsr"]
            lib.VeAPI_b_MinTempSnsr_DR = each_time_step["Inputs"]["MinTempSnsr_DR"]
            lib.VeAPI_T_MaxTempSnsr = each_time_step["Inputs"]["MaxTempSnsr"]
            lib.VeAPI_b_MaxTempSnsr_DR = each_time_step["Inputs"]["MaxTempSnsr_DR"]
            lib.VeAPI_Cap_ChgPackCapcty = each_time_step["Inputs"]["ChgPackCapcty"]
            lib.VeAPI_b_ChgPackCapcty_DR = each_time_step["Inputs"]["ChgPackCapcty_DR"]
            lib.VeAPI_Pct_PackSOC = each_time_step["Inputs"]["PackSOC"]
            lib.VeAPI_b_PackSOC_DR = each_time_step["Inputs"]["PackSOC_DR"]
            battery_state = each_time_step["Inputs"]["battery_state"]
            lib.VeAPI_b_EVSEChgStatus = each_time_step["Inputs"]["EVSEChgStatus"]

            # Run Function
            # ------------------------------------------------
            lib.Qnovo_AFC_1000ms(
                ffi.addressof(lib, "Host_Inputs"), ffi.addressof(lib, "AFC_Outputs")
            )

            lib.MaccorLogData_wrapper()

            # Record results
            results["Filename"].append(test_filename)
            results["Time"].append(input_time)
            results["PackCurr"].append(lib.VeAPI_I_PackCurr)
            results["PackCurr_DR"].append(lib.VeAPI_b_PackCurr_DR)
            results["SEVolts"].append(lib_array_to_list(lib.VaAPI_U_SEVolts))
            results["SEVolts_DR"].append(lib_array_to_list(lib.VaAPI_b_SEVolts_DR))
            results["TempSnsrs"].append(lib_array_to_list(lib.VaAPI_T_TempSnsrs))
            results["TempSnsrs_DR"].append(lib_array_to_list(lib.VaAPI_b_TempSnsrs_DR))
            results["MinTempSnsr"].append(lib.VeAPI_T_MinTempSnsr)
            results["MinTempSnsr_DR"].append(lib.VeAPI_b_MinTempSnsr_DR)
            results["MaxTempSnsr"].append(lib.VeAPI_T_MaxTempSnsr)
            results["MaxTempSnsr_DR"].append(lib.VeAPI_b_MaxTempSnsr_DR)
            results["ChgPackCapcty"].append(lib.VeAPI_Cap_ChgPackCapcty)
            results["ChgPackCapcty_DR"].append(lib.VeAPI_b_ChgPackCapcty_DR)
            results["PackSOC"].append(lib.VeAPI_Pct_PackSOC)
            results["PackSOC_DR"].append(lib.VeAPI_b_PackSOC_DR)
            results["Battery_State"].append(battery_state)
            results["EVSEChgStatus"].append(lib.VeAPI_b_EVSEChgStatus)
            results[" "].append("")  # Divider between input and output
            results["WarningFlags (dec)"].append(lib.VeAFC_e_WarningFlags)
            results["WarningFlags (bin)"].append(
                format(lib.VeAFC_e_WarningFlags, "032b")
            )
            results["ChgPackCurr"].append(lib.VeAFC_I_ChgPackCurr)
            results["ChgPackVolt"].append(lib.VeAFC_U_ChgPackVolt)
            results["ChgCompletionFlag"].append(lib.VeAFC_b_ChgCompletionFlag)

            results["QnovoAFC_LogVar1\nl_LoggingPath (dec)"].append(
                lib.QnovoAFC_LogVar1
            )
            results["QnovoAFC_LogVar1\nl_LoggingPath (bin)"].append(
                format(lib.QnovoAFC_LogVar1, "032b")
            )

            results["QnovoAFC_LogVar2\nl_InitializedFlag"].append(lib.QnovoAFC_LogVar2)

            results["QnovoAFC_LogVar3\nl_ValidSampleFlag"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar3)
            )

            results["QnovoAFC_LogVar4\nl_QNS_State"].append(lib.QnovoAFC_LogVar4)
            results["QnovoAFC_LogVar5\nl_PresentStageNum"].append(lib.QnovoAFC_LogVar5)
            results["QnovoAFC_LogVar6\nl_HighestIndex"].append(lib.QnovoAFC_LogVar6)
            results["QnovoAFC_LogVar7\nl_CCCPS_Index"].append(lib.QnovoAFC_LogVar7)
            results["QnovoAFC_LogVar8\nl_CCCPS_Stage"].append(lib.QnovoAFC_LogVar8)
            results["QnovoAFC_LogVar9\nl_CPVCorrIdx"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar9)
            )
            results["QnovoAFC_LogVar10\nl_CV_Curr"].append(lib.QnovoAFC_LogVar10)
            results["QnovoAFC_LogVar11\nl_CalcCurrForStage"].append(
                lib.QnovoAFC_LogVar11
            )
            results["QnovoAFC_LogVar12\nl_PreChgCurr"].append(lib.QnovoAFC_LogVar12)
            results["QnovoAFC_LogVar13\nl_PostChgCurr"].append(lib.QnovoAFC_LogVar13)
            results["QnovoAFC_LogVar14\nl_Post_Volt"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar14)
            )
            results["QnovoAFC_LogVar15\nl_SampleSEVolt"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar15)
            )
            results["QnovoAFC_LogVar16\nl_RefSEVolt"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar16)
            )

        _SUBDIR_NAME1 = "time_based_data\\output_data"
        dir_path = join(dirname(_MODULE_PATH), _SUBDIR_NAME1)
        res_path = join(dir_path, f"processed_{_FILENAME}")

        write_output_to_excel(results, res_path)

        _SUBDIR_NAME1 = "time_based_data\\reference_data"
        dir_path = join(dirname(_MODULE_PATH), _SUBDIR_NAME1)
        ref_path = join(dir_path, f"reference_{_FILENAME}")
        res_data = parse_AFC_Behavioral_Test_data(res_path)
        ref_data = parse_AFC_Behavioral_Test_data(ref_path)
        if not validate_with_reference_data(res_data, ref_data):
            pytest.fail(
                "Result data vs Reference data mismatch, see logs for exact mismatch"
            )
