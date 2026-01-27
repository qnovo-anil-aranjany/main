"""Test Module Description:
    Test module for 'AFC_CompensatedVoltage' functions in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_CompensatedVoltage'
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
                    "VeAPI_Pct_PackSOC": 6371,
                    "VaAPI_U_SEVolts": [3200] * 10,
                    "VaAPI_T_TempSnsrs": [350] * 4,
                },
                "Expected": {"Le_U_CompensatedSEVolt": 3028},
            },
            id="Test_Case_1",
            marks=[
                mark.description(
                    "This checks for how voltage is compensated given a cell current and temperature."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 1033,
                    "VaAPI_U_SEVolts": [3535] * 10,
                    "VaAPI_T_TempSnsrs": [266] * 4,
                },
                "Expected": {"Le_U_CompensatedSEVolt": 3600},
            },
            id="Test_Case_1",
            marks=[
                mark.description("Match On Chang calculations."),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_SOCtoOCV, AFC_CalcTemperatureRatio, from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - Le_U_CompensatedCellVolt,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_CompensatedVoltage

        parent_suite: swc_fast_charge
        suite: afc_compensated_voltage
        sub_suite: compensated_voltage
    """
)
def test_AFC_CompensatedVoltage(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_CompensatedVoltage'
    function.
    """

    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    Le_U_CellOCV = lib.AFC_SOCtoOCV(lib.VeAPI_Pct_PackSOC)
    Le_r_TemperatureRatio = lib.AFC_CalcTemperatureRatio(lib.VaAPI_T_TempSnsrs[0])
    Le_r_CurrRatio = lib.AFC_CalcCurrRatio()

    # Run Function
    # ------------------------------------------------
    Le_U_CompensatedSEVolt = lib.AFC_CompensatedVoltage(
        lib.VaAPI_U_SEVolts[0], Le_U_CellOCV, Le_r_TemperatureRatio, Le_r_CurrRatio
    )

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_CompensatedVoltage")
    logger.info(f"ACTUAL: Le_U_CompensatedSEVolt={Le_U_CompensatedSEVolt}")
    # Compare Result
    # ------------------------------------------------
    compare_result(
        test_cases["Expected"]["Le_U_CompensatedSEVolt"],
        Le_U_CompensatedSEVolt,
    )


# =======================================================================
# Stack-Parametrize Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "VeAPI_Pct_PackSOC": [x for x in range(0, 10000, 1000)],
        "VaAPI_U_SEVolts": [([x] * 10) for x in range(0, 4500, 500)],
        "VaAPI_T_TempSnsrs": [([x] * 4) for x in range(0, 600, 100)],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_SOCtoOCV, AFC_CalcTemperatureRatio, from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from json result file",\
            Step5: Test result should match with expected value,

            Source_File_In_Test: swc_afc_algo.c
            Method_In_Test: AFC_CompensatedVoltage

            parent_suite: swc_fast_charge
            suite: afc_compensated_voltage
            sub_suite: compensated_voltage_coverage
            label: Integration
        """
    )
    def test_AFC_CompensatedVoltage_coverage(
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

        Le_U_CellOCV = lib.AFC_SOCtoOCV(lib.VeAPI_Pct_PackSOC)
        Le_r_TemperatureRatio = lib.AFC_CalcTemperatureRatio(lib.VaAPI_T_TempSnsrs[0])
        Le_r_CurrRatio = lib.AFC_CalcCurrRatio()

        # Run Function
        # ------------------------------------------------
        Le_U_CompensatedSEVolt = lib.AFC_CompensatedVoltage(
            lib.VaAPI_U_SEVolts[0],
            Le_U_CellOCV,
            Le_r_TemperatureRatio,
            Le_r_CurrRatio,
        )

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_CompensatedVoltage")
        logger.info(f"ACTUAL: Le_U_CompensatedSEVolt={Le_U_CompensatedSEVolt}")
        dict_record = {"Le_U_CompensatedSEVolt": Le_U_CompensatedSEVolt}

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
