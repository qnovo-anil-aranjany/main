"""Test Module Description:
    Test module for 'AFC_ColdTempCompensation' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_ColdTempCompensation'
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
                "Inputs": {"Le_T_CellTemp": -10},
                "Expected": {"Le_U_CompensatedCurr": 5176},
            },
            id="Test_Case_1",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is -1.0 celsius."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_T_CellTemp": 0},
                "Expected": {"Le_U_CompensatedCurr": 5239},
            },
            id="Test_Case_2",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is 0 celsius."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_T_CellTemp": 150},
                "Expected": {"Le_U_CompensatedCurr": 6848},
            },
            id="Test_Case_3",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is 15.0 celsius."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_T_CellTemp": 340},
                "Expected": {"Le_U_CompensatedCurr": 9845},
            },
            id="Test_Case_4",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is 34.0 celsius."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_T_CellTemp": 350},
                "Expected": {"Le_U_CompensatedCurr": 10000},
            },
            id="Test_Case_5",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is 35.0 celsius."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"Le_T_CellTemp": 32767},
                "Expected": {"Le_U_CompensatedCurr": 10000},
            },
            id="Test_Case_6",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is at unrealistically high value."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110, QAFC-93

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_ColdTempCompensation from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - Le_U_CompensatedCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_ColdTempCompensation

        parent_suite: swc_fast_charge
        suite: afc_cold_temp_compensation
        sub_suite: cold_temp_compensation
    """
)
# NOTE: The results from the higher temp and lower temp are the same
def test_AFC_ColdTempCompensation(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_ColdTempCompensation'
    function.
    """

    # Setup Variables
    # ------------------------------------------------
    chg_current = 10000
    Le_T_CellTemp = test_cases["Inputs"]["Le_T_CellTemp"]

    # Run Function
    # ------------------------------------------------
    Le_U_CompensatedCurr = lib.AFC_ColdTempCompensation(chg_current, Le_T_CellTemp)

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_ColdTempCompensation")
    logger.info(f"ACTUAL: {Le_U_CompensatedCurr}")

    # Compare Results
    # ------------------------------------------------
    compare_result(test_cases["Expected"]["Le_U_CompensatedCurr"], Le_U_CompensatedCurr)


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "AFC_Param.Ke_k_ColdCompCoeff_a": 0.00011866,  # New: 0.00011866, Old: 0.00012517
                    "AFC_Param.Ke_k_ColdCompCoeff_b": -0.02089035,  # New: -0.02089035, Old: -0.01533200
                    "AFC_Param.Ke_T_ReferenceTemp": 250,
                    "AFC_Calc.Ve_T_StdU_RefCellTemp": 250.0 / 10.0,
                    "Le_T_CellTemp": 247,
                    "Le_I_ChgCurr": 214000,
                },
                "Expected": {"Le_U_CompensatedCurr": 212656},
            },
            id="Test_Case_7_Match",
            marks=[
                mark.description(
                    "This test checks if this function matches On Chang's expected results."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110, QAFC-93

        Steps:\
        Step1: StepHave the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_ColdTempCompensation from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - Le_U_CompensatedCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_ColdTempCompensation

        parent_suite: swc_fast_charge
        suite: afc_cold_temp_compensation
        sub_suite: cold_tempcompensation_behaviour
        label: Integration
    """
)
# NOTE: The results from the higher temp and lower temp are the same
def test_AFC_ColdTempCompensation_behavioral(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the
    'AFC_ColdTempCompensation' function.
    """

    # Setup Variables
    # ------------------------------------------------
    Le_I_ChgCurr = test_cases["Inputs"]["Le_I_ChgCurr"]
    Le_T_CellTemp = test_cases["Inputs"]["Le_T_CellTemp"]
    set_lib_inputs(lib, test_cases)

    # Run Function
    # ------------------------------------------------
    Le_U_CompensatedCurr = lib.AFC_ColdTempCompensation(Le_I_ChgCurr, Le_T_CellTemp)

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_ColdTempCompensation")
    logger.info(f"ACTUAL: Le_U_CompensatedCurr={Le_U_CompensatedCurr}")

    # Compare Results
    # ------------------------------------------------
    compare_result(test_cases["Expected"]["Le_U_CompensatedCurr"], Le_U_CompensatedCurr)


# =======================================================================
# Stack-Parametrize Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "chg_current": [x for x in range(0, 10000, 500)],
        "Cell_temp": [x for x in range(0, 600, 50)],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110, QAFC-93

            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: StepInvoke method AFC_ColdTempCompensation from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from json result file for specific test input param,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: swc_afc_algo.c
            Method_In_Test: AFC_ColdTempCompensation

            parent_suite: swc_fast_charge
            suite: afc_cold_temp_compensation
            sub_suite: cold_tempcompensation_coverage
            label: Integration
        """
    )
    def test_AFC_ColdTempCompensation_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input conditions to achieve improved
        code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        chg_current = test_cases["Inputs"]["chg_current"]
        Cell_temp = test_cases["Inputs"]["Cell_temp"]

        # Run Function
        # ------------------------------------------------
        Le_U_CompensatedCurr = lib.AFC_ColdTempCompensation(chg_current, Cell_temp)

        dict_record = {"Le_U_CompensatedCurr": Le_U_CompensatedCurr}

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_ColdTempCompensation")
        logger.info(f"ACTUAL: Le_U_CompensatedCurr={Le_U_CompensatedCurr}")
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
