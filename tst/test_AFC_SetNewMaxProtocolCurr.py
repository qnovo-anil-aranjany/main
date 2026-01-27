"""Test Module Description:
    Test module for 'AFC_MainPrdc' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_MainPrdc'
    functions for the fast charging algorithm works as expected under various scenarios.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""


from .main import *

ffi = cffi.FFI()

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

RUN_STACK_PARAM_TESTS = True  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = True  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)
MAKE_HTML = True
if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "alpha": 0.1,
                },
                "Expected": {
                    "AFC_Tunable_Param.Ka_I_Stg_ChgMaxCurr": [
                        345000,
                        345000,
                        345000,
                        345000,
                        345000,
                        345000,
                        int(311000 * 1.1),
                        int(290000 * 1.1),
                        int(270000 * 1.1),
                        int(251000 * 1.1),
                        int(232000 * 1.1),
                        int(214000 * 1.1),
                        int(197000 * 1.1),
                        int(180000 * 1.1),
                        int(165000 * 1.1),
                        int(150000 * 1.1),
                        int(136000 * 1.1),
                        int(123000 * 1.1),
                        int(111000 * 1.1),
                        int(100000 * 1.1),
                        int(90000 * 1.1),
                        81000,
                        72000,
                        61000,
                        50000,
                    ],
                },
            },
            id="Test_Case_1_Alpha_0.1",
            marks=[
                mark.description(
                    "This test checks if the tunable max protocol current would be scaled properly when alpha = 0.1"
                ),
                mark.jira_id("QAFC-252"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-252

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_SetNewMaxProtocolCurr from afc binary via cffi.,\
        Step4: compare output with expected value from input param - Le_I_Stg_ChgCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: qnovo_afc_features.c:
        Method_In_Test: AFC_SetNewMaxProtocolCurr

        parent_suite: swc_fast_charge
        suite: afc_set_new_max_protocol_curr
        sub_suite: set_new_max_protocol_curr
    """
)
def test_AFC_SetNewMaxProtocolCurr(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_MainPrdc' function.
    """

    # Setup Variables
    # ------------------------------------------------
    alpha = test_cases["Inputs"]["alpha"]
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    lib.AFC_SetNewMaxProtocolCurr(alpha)

    # Use these lines for updating testrail when required
    # log_for_testrail_update
    logger.info(
        f"ACTUAL: "
        f"AFC_Param.Ke_n_NumCPVStages={lib.AFC_Param.Ke_n_NumCPVStages},"
        f"AFC_Param.Ka_I_Stg_ChgMaxCurr={lib.AFC_Param.Ka_I_Stg_ChgMaxCurr},"
        f"AFC_HWLimits.Ke_I_MaxChgCurr={lib.AFC_HWLimits.Ke_I_MaxChgCurr},"
        f"AFC_Tunable_Param.Ka_I_Stg_ChgMaxCurr={lib.AFC_Tunable_Param.Ka_I_Stg_ChgMaxCurr},"
    )

    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)


# # =======================================================================
# # Stack-Parametrized Test Cases for Code Coverage
# # =======================================================================
# if RUN_STACK_PARAM_TESTS:
#     param_inputs = {
#         "VeAPI_Pct_PackSOC": [50, 7900, 10000],
#         "AFC_Calc.Ve_Cnt_PresentStgNum": [0, 20, 22, 25],
#         "AFC_Calc.Ve_e_QNS_State": [0, 1, 2],
#         "VaAPI_U_SEVolts": [([x] * 10) for x in [0, 3500, 4200, 4500]],
#         "VeAPI_T_MinTempSnsr": [0, 360],
#         "VeAPI_T_MaxTempSnsr": [550, 990],
#         "INP_Snsr.Ke_n_NumCellSeries": [1, 10],
#         "Le_b_CPVTrackingFlag": [0, 1],
#     }
#
#     combinations, ids = parametrize_args(param_inputs)
#
#     @pytest.mark.parametrize("test_cases", combinations, ids=ids)
#     @pytest.mark.jira_id("VCCFC-110")
#     @generate_requirement_link("QAFC-90")
#     @generate_requirement_link("QAFC-91")
#     @generate_requirement_link("QAFC-92")
#     @generate_requirement_link("QAFC-93")
#     @generate_requirement_link("QAFC-94")
#     @generate_requirement_link("QAFC-95")
#     @generate_requirement_link("QAFC-96")
#     @generate_requirement_link("QAFC-97")
#     @generate_requirement_link("QAFC-98")
#     @generate_requirement_link("QAFC-99")
#     @generate_requirement_link("QAFC-100")
#     @generate_requirement_link("QAFC-102")
#     @generate_requirement_link("QAFC-104")
#     @generate_requirement_link("QAFC-105")
#     @generate_requirement_link("QAFC-106")
#     @generate_requirement_link("QAFC-107")
#     @generate_requirement_link("QAFC-108")
#     @generate_requirement_link("QAFC-109")
#     @generate_requirement_link("QAFC-110")
#     @generate_requirement_link("QAFC-111")
#     @generate_requirement_link("QAFC-112")
#     @generate_requirement_link("QAFC-110", "[Requirement_Id - Everything]:")
#     @allure.feature(
#         "Step1: Have the source files ready for generating binary for swc_fast_charge. "
#         "Step2: Generate binary (shared dll using cmake) using cmake"
#         "Step3: Invoke method AFC_MainPrdc from afc binary via cffi using input param Le_T_CellTemp "
#         "Step4: compare output with expected value from result json file"
#         "Step5: Test result should match with expected value"
#     )
#     @allure.parent_suite("swc_fast_charge")
#     @allure.suite("afc_main_prdc")
#     @allure.sub_suite("main_prdc_coverage")
#     def test_AFC_MainPrdc_coverage(
#         lib, setup_parameters, test_cases, read_json_results, write_json_results
#     ) -> None:
#         """
#         This test function executes stack parametrization tests across a range of input conditions to achieve improved
#         code coverage.
#         """
#
#         # Setup Variables
#         # ------------------------------------------------
#         tracking_flag = test_cases["Inputs"]["Le_b_CPVTrackingFlag"]
#         set_lib_inputs(lib, test_cases)
#
#         lib.AFC_SetInputs(
#             ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
#         )
#
#         # Run Function
#         # ------------------------------------------------
#         lib.AFC_MainPrdc(tracking_flag)
#
#         # Compare Results
#         # ------------------------------------------------
#         if not WRITE_STACK_PARAM_RESULTS:
#             if lib.AFC_Calc.Ve_I_CV_Curr >= 1590138752:
#                 pytest.xfail(
#                     "Known issue where signed to unsigned changes 'AFC_Calc.Ve_I_CV_Curr' results from -1000A."
#                 )
#             else:
#                 validate_test_cases(lib, test_cases, read_json_results)
#
#         # Use these lines for updating testrail when required
#         # log_for_testrail_update("AFC_MainPrdc")
#         logger.info(
#             f"ACTUAL: AFC_Calc.Ve_e_QNS_State={lib.AFC_Calc.Ve_e_QNS_State},"
#             f"AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
#             f"AFC_Calc.Ve_I_CV_Curr={lib.AFC_Calc.Ve_I_CV_Curr},"
#             f"AFC_Calc.Va_b_ValidSampleFlag={lib.AFC_Calc.Va_b_ValidSampleFlag},"
#             f"AFC_Calc.Va_U_SampleSEVolt={lib.AFC_Calc.Va_U_SampleSEVolt},"
#             f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt},"
#             f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
#         )
#         # Log Stack-Parametrized Inputs
#         # ------------------------------------------------
#         if MAKE_HTML and LOG_STACK_PARAM_INPUTS:
#             log_stack_parametrized_inputs(test_cases)
#
#         # Optional: Log Stack-Parametrized Test Data
#         # JSON file can be found in /buildoutputs/reports
#         # ------------------------------------------------
#         if WRITE_STACK_PARAM_RESULTS:
#             vars_record = [
#                 "AFC_Calc.Ve_e_QNS_State",
#                 "AFC_Calc.Ve_Cnt_PresentStgNum",
#                 "AFC_Calc.Ve_I_CV_Curr",
#                 "AFC_Calc.Va_b_ValidSampleFlag",
#                 "AFC_Calc.Va_U_SampleSEVolt",
#                 "VeAFC_U_ChgPackVolt",
#                 "VeAFC_I_ChgPackCurr",
#             ]
#
#             record_test_data(
#                 lib, test_cases, write_json_results, var_to_record=vars_record
#             )
