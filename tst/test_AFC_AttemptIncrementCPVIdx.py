"""Test Module Description:
    Test module for 'AFC_AttemptIncrementCPVIdx' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_AttemptIncrementCPVIdx'
    functions for the fast charging algorithm works as expected under various scenarios.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""
from .main import *

MAKE_HTML = True
# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

RUN_STACK_PARAM_TESTS = True  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = True  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)

if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {"Le_i_CPV_PresentIndex": 0},
                "Expected": {"Le_i_NewIndex": 1},
            },
            id="Test_Case_1",
            marks=[
                mark.description(
                    "This checks for the 'Le_i_NewIndex' when stage = 10 and 'Le_i_CPV_PresentIndex' = 0."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_i_CPV_PresentIndex": 8},
                "Expected": {"Le_i_NewIndex": 9},
            },
            id="Test_Case_2",
            marks=[
                mark.description(
                    "This checks for the 'Le_i_NewIndex' when stage = 10 and 'Le_i_CPV_PresentIndex' = 8."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_i_CPV_PresentIndex": 18},
                "Expected": {"Le_i_NewIndex": 19},
            },
            id="Test_Case_3",
            marks=[
                mark.description(
                    "This checks for the 'Le_i_NewIndex' when stage = 10 and 'Le_i_CPV_PresentIndex' = 18."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_i_CPV_PresentIndex": 19},
                "Expected": {"Le_i_NewIndex": 19},
            },
            id="Test_Case_4",
            marks=[
                mark.description(
                    "This checks for the 'Le_i_NewIndex' when stage = 10 and 'Le_i_CPV_PresentIndex' = 19."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_i_CPV_PresentIndex": 100},
                "Expected": {"Le_i_NewIndex": 100},
            },
            id="Test_Case_5",
            marks=[
                mark.description(
                    "This checks for the 'Le_i_NewIndex' when stage = 10 and 'Le_i_CPV_PresentIndex' = 100."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_i_CPV_PresentIndex": 254},
                "Expected": {"Le_i_NewIndex": 254},
            },
            id="Test_Case_6",
            marks=[
                mark.description(
                    "This checks for the 'Le_i_NewIndex' when 'Le_i_CPV_PresentIndex' becomes unrealistically high."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_i_CPV_PresentIndex": 255},
                "Expected": {"Le_i_NewIndex": 0},
            },
            id="Test_Case_7",
            marks=[
                mark.description(
                    "This checks for the 'Le_i_NewIndex' when 'Le_i_CPV_PresentIndex' reach max unsigned char value, "
                    "integer overflow in Le_i_NewIndex should reset to zero as it cannot represent 256."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-92,QAFC-105, QAFC-106, QAFC-107

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake, \
        Step3: Invoke method AFC_AttemptIncrementCPVIdx from afc binary via cffi using input param Le_T_CellTemp ,\
        Step4: compare output with expected value from input param - Le_i_NewIndex,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_AttemptIncrementCPVIdx

        parent_suite: swc_fast_charge
        suite: afc_attempt_increment_cpvidx
        sub_suite: attempt_increment_cpvidx
    """
)
def test_AFC_AttemptIncrementCPVIdx(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the
    'AFC_AttemptIncrementCPVIdx' function.
    """

    # Setup Variables
    # ------------------------------------------------
    lib.AFC_Calc.Ve_Cnt_PresentStgNum = 10
    Le_i_CPV_PresentIndex = test_cases["Inputs"]["Le_i_CPV_PresentIndex"]

    # Run Function
    # ------------------------------------------------
    Le_i_NewIndex = lib.AFC_AttemptIncrementCPVIdx(Le_i_CPV_PresentIndex)

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_AttemptIncrementCPVIdx")
    logger.info(f"ACTUAL: Le_i_NewIndex={Le_i_NewIndex}")

    # Compare Result
    # ------------------------------------------------
    compare_result(test_cases["Expected"]["Le_i_NewIndex"], Le_i_NewIndex)


# =======================================================================
# Stack-Parametrize Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "Le_i_PresentStageIdx": [x for x in range(0, 41, 2)],
        "AFC_Calc.Ve_Cnt_PresentStgNum": [x for x in range(0, 25, 2)],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            JIRA-ID: QAFC-92,QAFC-105, QAFC-106, QAFC-107

            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge. ,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_AttemptIncrementCPVIdx from afc binary via cffi using input param Le_T_CellTemp ,\
            Step4: compare output with expected value from input param - Le_i_NewIndex,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: swc_afc_algo.c
            Method_In_Test: AFC_AttemptIncrementCPVIdx

            parent_suite: swc_fast_charge
            suite: afc_attempt_increment_cpvidx
            sub_suite: attempt_increment_cpvidx
            label: Integration
        """
    )
    def test_AFC_AttemptIncrementCPVIdx_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input conditions to achieve improved
        code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        Le_i_PresentStageIdx = test_cases["Inputs"]["Le_i_PresentStageIdx"]

        set_lib_inputs(lib, test_cases)

        # Run Function
        # ------------------------------------------------
        Le_i_NewIndex = lib.AFC_AttemptIncrementCPVIdx(Le_i_PresentStageIdx)

        dict_record = {"Le_i_NewIndex": Le_i_NewIndex}

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_AttemptIncrementCPVIdx")
        logger.info(f"ACTUAL: Le_i_NewIndex={Le_i_NewIndex}")

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
