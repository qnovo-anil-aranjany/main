"""Test Module Description:
    Test module for 'AFC_CPVTrack' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_CPVTrack'
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
ffi = cffi.FFI()
MAKE_HTML = True

if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3900] * 10,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [5] * 10,
                    "AFC_Calc.Va_U_RefSEVolt": [3100] * 10,
                },
                "Expected": {
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [6] * 10,
                    "AFC_Calc.Va_U_RefSEVolt": [3105] * 10,
                },
            },
            id="Test_Case_1_Tracking",
            marks=[
                mark.description(
                    "This checks the condition when CPV tracking is active, 'AFC_Calc.Va_Cnt_CPVCorrIdx' is "
                    "incremented by one and 'sAFC_Calc.Va_U_RefSEVolt' was correctly calculated."
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
        Step3: Invoke method AFC_CPVTrack from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - sAFC_Calc.Va_Cnt_CPVCorrIdx
        sAFC_Calc.Va_U_RefCellVolt,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: qnovo_afc_features.c
        Method_In_Test: AFC_CPVTrack

        parent_suite: swc_fast_charge
        suite: afc_cpv_track
        sub_suite: cpv_track
    """
)
def test_AFC_CPVTrack(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_CPVTrack'
    function.
    """

    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    lib.AFC_CPVTrack()

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_CPVTrack")
    logger.info(
        f"ACTUAL: AFC_Calc.Va_Cnt_CPVCorrIdx{lib.AFC_Calc.Va_Cnt_CPVCorrIdx},"
        f"AFC_Calc.Va_U_RefSEVolt: {lib.AFC_Calc.Va_U_RefSEVolt}"
    )
    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)


# =======================================================================
# Stack-Parametrize Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "AFC_Calc.Ve_Cnt_PresentStgNum": [0, 5, 10],
        "AFC_Calc.Va_b_ValidSampleFlag": [
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        ],
        "AFC_Calc.Va_U_SampleSEVolt": [
            [2750, 250, 1000, 2000, 1250, 3750, 2500, 3500, 500, 750],
            [3500, 3000, 3250, 1500, 4500, 4000, 0, 4250, 3750, 2750],
            [4500, 2500, 3250, 250, 4000, 3000, 500, 2750, 1250, 4250],
            [0, 2750, 1500, 250, 3250, 2250, 1750, 1250, 500, 1000],
        ],
        "AFC_Calc.Va_Cnt_CPVCorrIdx": [
            [19, 58, 42, 21, 45, 97, 81, 71, 80, 96],
            [32, 86, 20, 15, 78, 6, 62, 61, 57, 3],
            [100, 6, 54, 53, 16, 90, 36, 71, 16, 3],
            [40, 15, 19, 43, 63, 5, 30, 74, 67, 10],
        ],
        "AFC_Calc.Va_U_RefSEVolt": [
            [2750, 250, 1000, 2000, 1250, 3750, 2500, 3500, 500, 750],
            [3500, 3000, 3250, 1500, 4500, 4000, 0, 4250, 3750, 2750],
            [4500, 2500, 3250, 250, 4000, 3000, 500, 2750, 1250, 4250],
            [500, 2000, 750, 1000, 3500, 2500, 2250, 1750, 1250, 2750],
            [0, 2750, 1500, 250, 3250, 2250, 1750, 1250, 500, 1000],
        ],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            JIRA-ID: QAFC-92, QAFC-105, QAFC-106, QAFC-107, QAFC-110

            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_CPVTrack from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from result json file"
            Step5: Test result should match with expected value,

            Source_File_In_Test: qnovo_afc_features.c
            Method_In_Test: AFC_CPVTrack

            parent_suite: swc_fast_charge
            suite: afc_cpv_track
            sub_suite: cpv_track_coverage
            label: Integration
        """
    )
    def test_AFC_CPVTrack_coverage(
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
        lib.AFC_CPVTrack()

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_CPVTrack")
        logger.info(
            f"ACTUAL: AFC_Calc.Va_Cnt_CPVCorrIdx{lib.AFC_Calc.Va_Cnt_CPVCorrIdx},"
            f"AFC_Calc.Va_U_RefSEVolt: {lib.AFC_Calc.Va_U_RefSEVolt}"
        )
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
            vars_record = [
                "AFC_Calc.Va_Cnt_CPVCorrIdx",
                "AFC_Calc.Va_U_RefSEVolt",
            ]

            record_test_data(
                lib, test_cases, write_json_results, var_to_record=vars_record
            )
