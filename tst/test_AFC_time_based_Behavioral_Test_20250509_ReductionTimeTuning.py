"""Test Module Description:
    Test module for HSD time-based testing.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""

import ast
from os.path import abspath, dirname, join
from typing import Any
from ..submodules.tool_test_automation.src.common.utils import size

import cffi
import pytest

from submodules.tool_test_automation.src.common.fixtures import lib
from submodules.tool_test_automation.src.common.utils import (
    iter_file,
    lib_array_to_list,
    validate_with_reference_data,
    write_output_to_excel,
)

SKIP_TEST = False
MAKE_HTML = True
if not SKIP_TEST:
    _FILENAME = "Behavioral_Test_20250509_ReductionTimeTuning.xlsx"
    _SUBDIR_NAME = "time_based_data"
    _SUBDIR_INPUT_DATA = "time_based_data\\input_data"
    _SUBDIR_OUTPUT_DATA = "time_based_data\\output_data"
    _SUBDIR_REFERENCE_DATA = "time_based_data\\reference_data"

    _MODULE_PATH = abspath(__file__)
    _DIR_PATH_INPUT_DATA = join(dirname(_MODULE_PATH), _SUBDIR_INPUT_DATA)
    _FILE_PATH_INPUT_DATA = join(_DIR_PATH_INPUT_DATA, _FILENAME)
    _DIR_PATH_OUTPUT_DATA = join(dirname(_MODULE_PATH), _SUBDIR_OUTPUT_DATA)
    _FILE_PATH_OUTPUT_DATA = join(_DIR_PATH_OUTPUT_DATA, f"processed_{_FILENAME}")
    _DIR_PATH_REFERENCE_DATA = join(dirname(_MODULE_PATH), _SUBDIR_REFERENCE_DATA)
    _FILE_PATH_REFERENCE_DATA = join(_DIR_PATH_REFERENCE_DATA, f"reference_{_FILENAME}")

    ffi = cffi.FFI()

    def parse_AFC_Behavioral_Test_data(file_path):
        test_cases = []
        for row in iter_file(file_path):
            test_filename = row["Filename"]
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

            battery_state = row["Battery_State"]
            EVSEChgStatus = int(row["EVSEChgStatus"])

            ActualChgTime = int(row["ActualChgTime"])
            DesiredChgTime = int(row["DesiredChgTime"])

            # Format data for parametrized test
            test_case = {
                "Inputs": {
                    "Filename": test_filename,
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
                    "Battery_State": battery_state,
                    "EVSEChgStatus": EVSEChgStatus,
                    "ActualChgTime": ActualChgTime,
                    "DesiredChgTime": DesiredChgTime,
                },
                "Expected": {},
            }

            test_cases.append(test_case)
        return test_cases

    def test_AFC_Behavioral_Test_20240423(lib: Any):
        all_time_steps = parse_AFC_Behavioral_Test_data(_FILE_PATH_INPUT_DATA)
        # Initialize results
        results = {
            "Filename": [],
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
            "ActualChgTime": [],
            "DesiredChgTime": [],
            " ": [],
            "WarningFlags (dec)": [],
            "WarningFlags (bin)": [],
            "ChgPackCurr": [],
            "ChgPackVolt": [],
            "ChgCompletionFlag": [],
            "AFC_NVM_MagicNumber": [],
            "AFC_CTE_MagicNumber": [],
            "AFC_CTE_HighestIndex": [],
            "NVM_HighestIndex": [],
            "NVM_HighestIndex2": [],
            "QnovoAFC_LogVar1\nl_LoggingPath (dec)": [],
            "QnovoAFC_LogVar1\nl_LoggingPath (bin)": [],
            "QnovoAFC_LogVar2\nl_InitializedFlag": [],
            "QnovoAFC_LogVar3\nl_ValidSampleFlag": [],
            "QnovoAFC_LogVar4\nl_QNS_State": [],
            "QnovoAFC_LogVar5\nl_PresentStageNum": [],
            "QnovoAFC_LogVar6\nl_HighestIndex": [],
            "QnovoAFC_LogVar9\nl_CPVCorrIdx": [],
            "QnovoAFC_LogVar10\nl_CV_Curr": [],
            "QnovoAFC_LogVar11\nl_ProtocolStgCurr": [],
            "QnovoAFC_LogVar13\nl_ColdCompensatedCurr": [],
            "QnovoAFC_LogVar14\nl_CompensatedVolt": [],
            "QnovoAFC_LogVar15\nl_SampleSEVolt": [],
            "QnovoAFC_LogVar16\nl_RefSEVolt": [],
            "QnovoAFC_LogVar7\nl_TuningAlpha": [],
            "AFC_Tunable_Param.Ka_I_Stg_ChgMaxCurr": [],
        }
        for each_time_step in all_time_steps:
            # Setup Variables
            # ------------------------------------------------
            test_filename = each_time_step["Inputs"]["Filename"]
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
            battery_state = each_time_step["Inputs"]["Battery_State"]
            lib.VeAPI_b_EVSEChgStatus = each_time_step["Inputs"]["EVSEChgStatus"]
            lib.VeAPI_t_ActualChgTime = each_time_step["Inputs"]["ActualChgTime"]
            lib.VeAPI_t_DesiredChgTime = each_time_step["Inputs"]["DesiredChgTime"]

            # Run Function
            # ------------------------------------------------
            lib.Qnovo_AFC(
                ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
            )

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
            results["ActualChgTime"].append(lib.VeAPI_t_ActualChgTime)
            results["DesiredChgTime"].append(lib.VeAPI_t_DesiredChgTime)
            results[" "].append("")  # Divider between input and output
            results["WarningFlags (dec)"].append(lib.VeAFC_e_WarningFlags)
            results["WarningFlags (bin)"].append(
                format(lib.VeAFC_e_WarningFlags, "032b")
            )
            results["ChgPackCurr"].append(lib.VeAFC_I_ChgPackCurr)
            results["ChgPackVolt"].append(lib.VeAFC_U_ChgPackVolt)
            results["ChgCompletionFlag"].append(lib.VeAFC_b_ChgCompletionFlag)

            results["AFC_NVM_MagicNumber"].append(lib.AFC_Track.Ne_b_InitNVMStatus)
            results["AFC_CTE_MagicNumber"].append(lib.AFC_CTE_Data.Ve_b_InitNVMStatusCTE)

            lib.LIB_Deobfuscate(ffi.addressof(lib.AFC_CTE_Data, "Va_Cnt_CPVCorrIdx"), size(lib.AFC_CTE_Data.Va_Cnt_CPVCorrIdx), 0xBD)
            results["AFC_CTE_HighestIndex"].append(lib_array_to_list(lib.AFC_CTE_Data.Va_Cnt_CPVCorrIdx))

            max_indices = [max(lib.AFC_Track.Nt_Cnt_CPVCorrIdx[i][j] for i in range(192)) for j in range(21)]
            results["NVM_HighestIndex"].append(max_indices)

            results["NVM_HighestIndex2"].append(lib_array_to_list(lib.AFC_Track.Na_Cnt_HighestCPVCorrIdx))

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
            results["QnovoAFC_LogVar9\nl_CPVCorrIdx"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar9)
            )
            results["QnovoAFC_LogVar10\nl_CV_Curr"].append(lib.QnovoAFC_LogVar10)
            results["QnovoAFC_LogVar11\nl_ProtocolStgCurr"].append(
                lib.QnovoAFC_LogVar11
            )
            results["QnovoAFC_LogVar13\nl_ColdCompensatedCurr"].append(lib.QnovoAFC_LogVar13)
            results["QnovoAFC_LogVar14\nl_CompensatedVolt"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar14)
            )
            results["QnovoAFC_LogVar15\nl_SampleSEVolt"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar15)
            )
            results["QnovoAFC_LogVar16\nl_RefSEVolt"].append(
                lib_array_to_list(lib.QnovoAFC_LogVar16)
            )
            results["QnovoAFC_LogVar7\nl_TuningAlpha"].append(lib.QnovoAFC_LogVar7)
            results["AFC_Tunable_Param.Ka_I_Stg_ChgMaxCurr"].append(list(lib.AFC_Tunable_Param.Ka_I_Stg_ChgMaxCurr))

        write_output_to_excel(results, _FILE_PATH_OUTPUT_DATA)

        res_data = parse_AFC_Behavioral_Test_data(_FILE_PATH_OUTPUT_DATA)
        ref_data = parse_AFC_Behavioral_Test_data(_FILE_PATH_REFERENCE_DATA)
        if not validate_with_reference_data(res_data, ref_data):
            pytest.fail(
                "Result data vs Reference data mismatch, see logs for exact mismatch"
            )
