"""Test Module Description:
    Test module for 'AFC_HighestCPVStageIdx' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_HighestCPVStageIdx'
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
MAKE_HTML = True
RUN_STACK_PARAM_TESTS = True  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = True  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)

ffi = cffi.FFI()

if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {"AFC_Calc.Va_Cnt_CPVCorrIdx": [i + 1 for i in range(10)]},
                "Expected": {
                    "highest_index": 10,
                },
            },
            id="Test_Case_1_HighestIndex",
            marks=[
                mark.description(
                    "This checks that the function return the highest index given 'AFC_Calc.Va_Cnt_CPVCorrIdx' "
                    "array."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: StepInvoke method AFC_HighestCPVStageIdx from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - highest_index,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: qnovo_afc_features.c
        Method_In_Test: AFC_CalcAlpha

        parent_suite: swc_fast_charge
        suite: afc_highest_cpvidx_present_stage
        sub_suite: highest_cpvidx_present_stage
        label: Unit
    """
)
def test_HighestCPVIdxPresentStage(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the
    'AFC_HighestCPVStageIdx' function.
    """

    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    highest_index = lib.AFC_HighestCPVStageIdx()

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_HighestCPVStageIdx")
    logger.info(f"ACTUAL: highest_index={highest_index}")

    # Compare Results
    # ------------------------------------------------
    compare_result(test_cases["Expected"]["highest_index"], highest_index)


# =======================================================================
# Stack-Parametrize Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "AFC_Calc.Va_Cnt_CPVCorrIdx": [
            [19, 58, 42, 21, 45, 97, 81, 71, 80, 96],
            [32, 86, 20, 15, 78, 6, 62, 61, 57, 3],
            [100, 6, 54, 53, 16, 90, 36, 71, 16, 3],
            [82, 81, 44, 72, 3, 54, 86, 15, 47, 16],
            [93, 11, 80, 15, 91, 88, 7, 40, 48, 91],
            [32, 7, 28, 45, 31, 12, 100, 56, 55, 7],
            [19, 86, 98, 10, 45, 65, 84, 43, 77, 87],
            [73, 36, 25, 86, 84, 79, 74, 61, 61, 49],
            [64, 81, 18, 41, 10, 4, 79, 31, 46, 45],
            [40, 15, 19, 43, 63, 5, 30, 74, 67, 10],
        ],
        "INP_Snsr.Ke_n_NumCellSeries": [0, 1, 5, 7, 10],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110

            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_HighestCPVStageIdx from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from result json file,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: qnovo_afc_features.c
            Method_In_Test: AFC_CalcAlpha

            parent_suite: swc_fast_charge
            suite: afc_highest_cpvidx_present_stage
            sub_suite: highest_cpvidx_present_stage_coverage
            label: Integration
        """
    )
    def test_HighestCPVIdxPresentStage_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input conditions to achieve improved
        code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        set_lib_inputs(lib, test_cases)

        # Run Function
        # ------------------------------------------------
        highest_index = lib.AFC_HighestCPVStageIdx()

        dict_record = {"highest_index": highest_index}

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_HighestCPVStageIdx")
        logger.info(f"ACTUAL: highest_index={highest_index}")
        # Compare Results
        # ------------------------------------------------
        if not WRITE_STACK_PARAM_RESULTS:
            validate_test_cases(
                lib, test_cases, read_json_results, dict_to_compare=dict_record
            )

        # Log Stack-Parametrized Inputs
        # ------------------------------------------------
        if MAKE_HTML and LOG_STACK_PARAM_INPUTS:
            log_stack_parametrized_inputs(test_cases)

        # Optional: Log Stack-Parametrized Test Data
        # JSON file can be found in /buildoutputs/reports
        # ------------------------------------------------
        if WRITE_STACK_PARAM_RESULTS:
            record_test_data(
                lib, test_cases, write_json_results, dict_to_record=dict_record
            )
