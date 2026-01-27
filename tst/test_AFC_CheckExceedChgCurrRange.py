"""Test Module Description:
    Test module for 'AFC_CheckExceedChgCurrRange' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_CheckExceedChgCurrRange'
    functions for the fast charging algorithm works as expected under various scenarios.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""

from .main import *

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.
RUN_STACK_PARAM_TESTS = False  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = True  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)
from pytest import fixture, mark, param

ffi = cffi.FFI()
MAKE_HTML = True

# Optional Flags:
# ------------------------------------------------

if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "VeAFC_I_ChgPackCurr": 345001,
                },
                "Expected": {
                    "VeAFC_e_WarningFlags": 4,
                    "VeAFC_I_ChgPackCurr": 0,
                },
            },
            id="TC1_ExceedMaxCurrent",
            marks=[
                mark.description(
                    "This test case verifies that the charge current limit is at 0A if the current limit exceed the "
                    "max allowable value MAX_CHG_CURR_RANGE."
                ),
                mark.jira_id("QAFC-51"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAFC_I_ChgPackCurr": 345000,
                },
                "Expected": {
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 345000,
                },
            },
            id="TC2_DoesNotExceedMaxCurrent",
            marks=[
                mark.description(
                    "This test case verifies that the charge current limit is at 0A if the current limit does not "
                    "exceed the max allowable value MAX_CHG_CURR_RANGE."
                ),
                mark.jira_id("QAFC-51"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-102

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_CheckExceedChgCurrRange from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - VeAFC_e_WarningFlags, VeAFC_I_ChgPackCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_warning.c
        Method_In_Test: AFC_CheckExceedChgCurrRange

        parent_suite: swc_fast_charge
        suite: afc_check_exceed_current_range
        sub_suite: check_exceed_current_range
    """
)
def test_AFC_CheckExceedChgCurrRange(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the
    'AFC_CheckChgCompletion' function.
    """

    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    lib.AFC_CheckExceedChgCurrRange()

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_CheckExceedChgCurrRange")
    logger.info(
        f"ACTUAL: VeAFC_e_WarningFlags={lib.VeAFC_e_WarningFlags},"
        f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
    )
    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)


# =======================================================================
# Stack-Parametrized Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "VeAPI_Pct_PackSOC": [50, 7900, 10000],
        "AFC_Calc.Ve_Cnt_PresentStgNum": [0, 20, 22, 25],
        "AFC_Calc.Ve_e_QNS_State": [0, 1, 2],
        "VaAPI_U_SEVolts": [([x] * 10) for x in [0, 3500, 4200, 4500]],
        "VeAPI_T_MinTempSnsr": [0, 360],
        "VeAPI_T_MaxTempSnsr": [550, 990],
        "INP_Snsr.Ke_n_NumCells": [1, 10],
        "Le_b_CPVTrackingFlag": [0, 1],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            JIRA-ID: QAFC-102

            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_CheckExceedChgCurrRange from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from json result file for specific test input param,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: swc_afc_warning.c
            Method_In_Test: AFC_MainPrdc

            parent_suite: swc_fast_charge
            suite: afc_check_exceed_current_range
            sub_suite: check_exceed_current_range_coverage
            label: Integration
        """
    )
    def test_AFC_MainPrdc_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input conditions to achieve improved
        code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        tracking_flag = test_cases["Inputs"]["Le_b_CPVTrackingFlag"]
        set_lib_inputs(lib, test_cases)

        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )

        # Run Function
        # ------------------------------------------------
        lib.AFC_MainPrdc(tracking_flag)

        logger.info(f"ACTUAL: TBD")
        # Compare Results
        # ------------------------------------------------
        if not WRITE_STACK_PARAM_RESULTS:
            if lib.sAFC_Calc.Ve_I_CV_Curr >= 1590138752:
                pytest.xfail(
                    "Known issue where signed to unsigned changes 'sAFC_Calc.Ve_I_CV_Curr' results from -1000A."
                )
            else:
                validate_test_cases(lib, test_cases, read_json_results)

        # Log Stack-Parametrized Inputs
        # ------------------------------------------------
        if MAKE_HTML and LOG_STACK_PARAM_INPUTS:
            log_stack_parametrized_inputs(test_cases)

        # Optional: Log Stack-Parametrized Test Data
        # JSON file can be found in /buildoutputs/reports
        # ------------------------------------------------
        if WRITE_STACK_PARAM_RESULTS:
            vars_record = [
                "AFC_Calc.Ve_e_QNS_State",
                "AFC_Calc.Ve_Cnt_PresentStgNum",
                "AFC_Calc.Ve_I_CV_Curr",
                "AFC_Calc.Va_b_ValidSampleFlag",
                "AFC_Calc.Va_U_SampleSEVolt",
                "VeAFC_U_ChgPackVolt",
                "VeAFC_I_ChgPackCurr",
            ]

            record_test_data(
                lib, test_cases, write_json_results, var_to_record=vars_record
            )

