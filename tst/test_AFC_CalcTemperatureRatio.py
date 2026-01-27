"""Test Module Description:
    Test module for 'AFC_CalcTemperatureRatio' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_CalcTemperatureRatio'
    functions for the fast charging algorithm works as expected under various scenarios.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""

from .main import *

ffi = cffi.FFI()
MAKE_HTML = True

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

RUN_STACK_PARAM_TESTS = False  # Set True to run stack-parametrized testing.
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
                "Inputs": {
                    "AFC_Param.Ke_k_ColdCompCoeff_a": 0.00045776,
                    "AFC_Param.Ke_k_ColdCompCoeff_b": -0.01351100,
                    "AFC_Param.Ke_k_ColdCompCoeff_c": 0.0000044631,
                    "AFC_Param.Ke_T_ReferenceTemp": 350,
                    "AFC_Calc.Ve_T_StdU_RefCellTemp": 350.0 / 10.0,
                    "Le_T_CellTemp": 250,
                },
                "Expected": {
                    "Le_r_TemperatureRatio": 1.212812991,
                },
            },
            id="Test_Case_1_MatchEquation",
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
        JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_CalcTemperatureRatio from afc binary via cffi using input param Le_T_CellTemp ,\
        Step4: compare output with expected value from input param - Le_r_TemperatureRatio,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: qnovo_afc_features.c
        Method_In_Test: AFC_CalcAlpha

        parent_suite: swc_fast_charge
        suite: afc_calc_temperature_ratio
        sub_suite: calc_temperature_ratio_behavioural
        label: Integration
    """
)
def test_AFC_CalcTemperatureRatio_behavioral(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the
    'AFC_CalcTemperatureRatio' function.
    """

    # Setup Variables
    # ------------------------------------------------
    Le_T_CellTemp = test_cases["Inputs"]["Le_T_CellTemp"]
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    Le_r_TemperatureRatio = lib.AFC_CalcTemperatureRatio(Le_T_CellTemp)

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_CalcTemperatureRatio")
    logger.info(f"ACTUAL: Le_r_TemperatureRatio={Le_r_TemperatureRatio}")

    # Compare Results
    # ------------------------------------------------
    compare_result(
        test_cases["Expected"]["Le_r_TemperatureRatio"], Le_r_TemperatureRatio
    )


# =======================================================================
# Stack-Parametrized Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {}

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110

            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_CalcTemperatureRatio from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from json result file for specific test input param,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: qnovo_afc_features.c
            Method_In_Test: AFC_CalcAlpha

            parent_suite: swc_fast_charge
            suite: afc_calc_temperature_ratio
            sub_suite: calc_temperature_ratio_coverage
            label: Integration
        """
    )
    def test_AFC_CalcTemperatureRatio_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input conditions to achieve improved
        code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        set_lib_inputs(lib, test_cases)

        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )

        # Run Function
        # ------------------------------------------------

        logger.info(f"ACTUAL: TBD")
        # Compare Results
        # ------------------------------------------------
        if not WRITE_STACK_PARAM_RESULTS:
            validate_test_cases(lib, test_cases, read_json_results)

        # Log Stack-Parametrized Inputs
        # ------------------------------------------------
        if MAKE_HTML and LOG_STACK_PARAM_INPUTS:
            log_stack_parametrized_inputs(test_cases)

        # Optional: Log Stack-Parametrized Test Data
        # JSON file can be found in /buildoutputs/reports
        # ------------------------------------------------
        if WRITE_STACK_PARAM_RESULTS:
            vars_record = []

            record_test_data(
                lib, test_cases, write_json_results, var_to_record=vars_record
            )
