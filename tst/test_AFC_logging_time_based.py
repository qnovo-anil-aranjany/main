
"""Test Module Description:
    Test module for HSD time-based testing.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.12.4
    - Pytest version >= 8.0.1
"""

from .main import *
from .main import (
    _MODULE_PATH,
    _TIME_BASED_INPUT_DATA,
    _TIME_BASED_OUTPUT_DATA,
    _TIME_BASED_REFERENCE_DATA,
)

ffi = cffi.FFI()
SKIP_TEST = False
MAKE_HTML = True
if not SKIP_TEST:
    _FILENAME = "AFC_Logging_Time_Based.xlsx"

    def parse_AFC_logging_test_data(file_path):
        test_cases = []
        i=0
        for row in iter_file(file_path):
            try:
                PackSOC = int(float(row["PackSOC"]) * 100)
                PackSOC_DR = int(row["PackSOC_DR"])
                PackCurr = int(float(row["PackCurr"]) * 2000)
                PackCurr_DR = int(row["PackCurr_DR"])
                try:
                    CellVolts = [
                        int(float(item) * 1000) for item in ast.literal_eval(row["SEVolts"])
                    ]
                except TypeError:
                    CellVolts = [int(row["SEVolts"])]

                try:
                    CellVolts_DR = [
                        int(item) for item in ast.literal_eval(row["SEVolts_DR"])
                    ]
                except TypeError:
                    CellVolts_DR = [int(row["SEVolts_DR"])]

                MinTempSnsr = int(float(row["MinTempSnsr"]) * 10)
                MinTempSnsr_DR = int(row["MinTempSnsr_DR"])

                MaxTempSnsr = int(float(row["MaxTempSnsr"]) * 10)
                MaxTempSnsr_DR = int(row["MaxTempSnsr_DR"])

                TempSnsrs = [MaxTempSnsr for _ in range(18)]
                TempSnsrs_DR = [1 for _ in range(18)]


                try:
                    ChgPackCapcty = int(float(row["ChgPackCapcty"]))
                except ValueError:
                    ChgPackCapcty = 0
                ChgPackCapcty_DR = int(row["ChgPackCapcty_DR"])


                battery_state = row["Battery_State"]
                EVSEChgStatus = int(row["EVSEChgStatus"])


            except KeyError:
                logger.error("Key not found in input data")

            # Format data for parametrized test
            test_case = {
                "Inputs": {
                    "PackSOC": PackSOC,
                    "PackSOC_DR": PackSOC_DR,
                    "PackCurr": PackCurr,
                    "PackCurr_DR": PackCurr_DR,
                    "CellVolts": CellVolts,
                    "CellVolts_DR": CellVolts_DR,
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
            i+=1
            if i > 1000:
                break

        return test_cases

    @pytest.mark.parametrize(
        "input_file_name, output_file_name, reference_file_name",
        [(_FILENAME, _FILENAME, _FILENAME)],
        indirect=True,
    )
    def test_AFC_logging_behavioral(
        lib: Any, input_file_name, output_file_name, reference_file_name
    ):


        all_time_steps = parse_AFC_logging_test_data(input_file_name)
        # Initialize results
        results = {
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
            "NVM_Warnings": [],
            "Ne_Cnt_ChargeCycleNum": [],
            "Ne_Cnt_SocIncrAccum": [],
            "Ne_b_EarlyAgingWarning": [],
            "Ne_b_AbnormalAging": [],
            "Ne_b_ExtremeAging": [],
            "Na_Cnt_HighestCPVCorrIdx": [],
        }
        # Initial log buffer
        process_log_buffer(lib, 0, True)
        for i in range(192):
            cpv_idx = f"NVM_CPVCorrIdx[{i}]"
            results[cpv_idx] = []

        row_count = 2
        logger.info(f"Warning Flags: {results["WarningFlags (dec)"]}")
        logger.info(f"Early Flags: {lib.AFC_Track.Ne_b_EarlyAgingWarning}")
        logger.info(f"Abnormal Flags: {lib.AFC_Track.Ne_b_AbnormalAging}")
        logger.info(f"Extreme Flags: {lib.AFC_Track.Ne_b_ExtremeAging}")

        count = 0
        final_output = []
        first = True
        for each_time_step in all_time_steps:
            #logger.info(each_time_step)
            output_file_name = input_file_name.replace("input", "output").replace(".xlsx", f"_{row_count}.csv")
            #logger.info(f"output_file_name: {output_file_name}")
            # Setup Variables
            # ------------------------------------------------
            lib.VeAPI_I_PackCurr = each_time_step["Inputs"]["PackCurr"]
            lib.VeAPI_b_PackCurr_DR = each_time_step["Inputs"]["PackCurr_DR"]
            lib.VaAPI_U_SEVolts = each_time_step["Inputs"]["CellVolts"]
            lib.VaAPI_b_SEVolts_DR = each_time_step["Inputs"]["CellVolts_DR"]
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
            lib.Qnovo_AFC(
                ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
            )

            # Record results
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
            results["Ne_Cnt_ChargeCycleNum"].append(lib.AFC_Track.Ne_Cnt_ChargeCycleNum)
            results["Ne_Cnt_SocIncrAccum"].append(lib.AFC_Track.Ne_Cnt_SocIncrAccum)
            results["Ne_b_EarlyAgingWarning"].append(lib.AFC_Track.Ne_b_EarlyAgingWarning)
            results["Ne_b_AbnormalAging"].append(lib.AFC_Track.Ne_b_AbnormalAging)
            results["Ne_b_ExtremeAging"].append(lib.AFC_Track.Ne_b_ExtremeAging)
            results["Na_Cnt_HighestCPVCorrIdx"].append(list(lib.AFC_Track.Na_Cnt_HighestCPVCorrIdx))

            cpvidx_result = [
                lib_array_to_list(i) for i in lib.AFC_Track.Nt_Cnt_CPVCorrIdx
            ]
            for i in range(192):
                cpv_idx = f"NVM_CPVCorrIdx[{i}]"
                results[cpv_idx] = cpvidx_result[i]

            final_output.append(copy.deepcopy(results))
            for key in results:
                results[key] = []

            row_count += 1
            count += 1
            if count == 10000:
                if first:
                    write_output_to_csv(final_output, output_file_name)
                    first = False
                else:
                    write_output_to_csv(final_output, output_file_name, True)
                final_output = []
                count = 0
                #process_log_buffer


        if count > 0:
            output_file_name = input_file_name.replace("input", "output").replace(".xlsx", "_last.csv")
            if first:
                write_output_to_csv(final_output, output_file_name)
                first = False
            else:
                write_output_to_csv(final_output, output_file_name, True)

        logger.info(f"Iteration : {row_count}")
        # Parse log buffer and get result data
        result = process_log_buffer(lib, 198, True)
        #result.print_buffer()

        #write_output_to_excel(results, output_file_name)
        #logger.info(f"Output file: {output_file_name}")
        '''
        res_data = parse_AFC_Behavioral_Test_data(output_file_name)
        logger.info(f"Reference file name : {reference_file_name}")
        ref_data = parse_AFC_Behavioral_Test_data(reference_file_name)
        if not validate_with_refrence_data(res_data, ref_data):
            pytest.fail(
                "Result data vs Reference data mismatch, see logs for exact mismatch"
            )
        '''
