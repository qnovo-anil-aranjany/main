"""Test Module Description:
    Test module for 'AFC_SOCtoOCV' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_SOCtoOCV'
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

ffi = cffi.FFI()


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 14,
                },
                "Expected": {
                    "Le_U_CellOCV": 3173,
                },
            },
            id="Test_Case_1",
            marks=[
                mark.description(
                    "Investigate issue pointed out by On Chang where terminal voltage was 3.159V while calculated OCV "
                    "was 3.173V... This is due to the insufficient range of OCV-SOC curve and also the fact that OCV "
                    "calculation is a simple look up of SOC and does not account for voltage."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 1033,
                },
                "Expected": {
                    "Le_U_CellOCV": 3412,
                },
            },
            id="Test_Case_2",
            marks=[
                mark.description("Match On Chang calculations."),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 0,
                },
                "Expected": {
                    "Le_U_CellOCV": 3165,
                },
            },
            id="Test_Case_3",
            marks=[
                mark.description("Test when SOC is at 0"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 10000,
                },
                "Expected": {
                    "Le_U_CellOCV": 4252,
                },
            },
            id="Test_Case_4",
            marks=[
                mark.description("Test when SOC is at 100%"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 10001,
                },
                "Expected": {
                    "Le_U_CellOCV": 4252,
                },
            },
            id="Test_Case_5",
            marks=[
                mark.description("Test when SOC is just over 100%"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 65535,
                },
                "Expected": {
                    "Le_U_CellOCV": 4252,
                },
            },
            id="Test_Case_6",
            marks=[
                mark.description("Test when SOC is way over 100%"),
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
        Step3: Invoke method AFC_SOCtoOCV from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - Le_U_CellOCV,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_SOCtoOCV

        parent_suite: swc_fast_charge
        suite: afc_soc_to_ocv
        sub_suite: soc_to_ocv
    """
)
def test_AFC_SOCtoOCV(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_SOCtoOCV' function.
    """

    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    # Run Function
    # ------------------------------------------------
    Le_U_CellOCV = lib.AFC_SOCtoOCV(lib.VeAPI_Pct_PackSOC)

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_SOCtoOCV")
    logger.info(f"ACTUAL: Le_U_CellOCV={Le_U_CellOCV}")
    # Compare Results
    # ------------------------------------------------
    compare_result(test_cases["Expected"]["Le_U_CellOCV"], Le_U_CellOCV)


@pytest.mark.parametrize("x", [x for x in range(0, 10500, 500)])
@allure.feature(
    """
        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_SOCtoOCV from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from calculated value by np.interp(lib.VeAPI_Pct_PackSOC \
        KaSHR_Pct_SOCAxis, KaSHR_U_OCVAxis,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_SOCtoOCV

        parent_suite: swc_fast_charge
        suite: afc_soc_to_ocv
        sub_suite: soc_to_ocv_coverage
        label: Integration
    """
)
def test_AFC_SOCtoOCV_coverage(lib, setup_parameters, x) -> None:
    """
    This test function executes stack parametrization tests across a range of input conditions to achieve improved
    code coverage.
    """

    # Setup Variables
    # ------------------------------------------------
    lib.VeAPI_Pct_PackSOC = x

    KaAFC_Pct_SOCAxis = lib_array_to_list(lib.KaAFC_Pct_SOCAxis)
    KaAFC_U_OCVAxis = lib_array_to_list(lib.KaAFC_U_OCVAxis)

    # Run Function
    # ------------------------------------------------
    expected_value = np.interp(
        lib.VeAPI_Pct_PackSOC, KaAFC_Pct_SOCAxis, KaAFC_U_OCVAxis
    )
    Le_U_CellOCV = lib.AFC_SOCtoOCV(lib.VeAPI_Pct_PackSOC)

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_SOCtoOCV")
    logger.info(f"ACTUAL: Le_U_CellOCV={Le_U_CellOCV}")

    compare_result(int(expected_value), Le_U_CellOCV)
