"""Test Module Description:
    Test module for 'AFC_MainInit' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_MainInit'
    functions for the fast charging algorithm works as expected under various scenarios.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""


from .main import *

# === Uncomment the following line to skip all test cases in this module: ===
# pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")

ffi = cffi.FFI()


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 9601,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3200] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 25,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3200] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 30000,
                },
            },
            id="Test_Case_1_Initialize",
            marks=[
                mark.description(
                    "This test runs the 'AFC_MainInit' function and checks if initializations was properly executed."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-91

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_MainInit from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - Le_I_Stg_ChgCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_MainInit

        parent_suite: swc_fast_charge
        suite: afc_main_init
        sub_suite: main_init
    """
)
def test_AFC_MainInit(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_MainInit' function.
    """

    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    lib.AFC_MainInit()

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_MainInit")
    logger.info(
        f"ACTUAL: AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
        f"AFC_Calc.Va_b_ValidSampleFlag={lib.AFC_Calc.Va_b_ValidSampleFlag},"
        f"AFC_Calc.Va_U_SampleSEVolt={lib.AFC_Calc.Va_U_SampleSEVolt},"
        f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt},"
        f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
    )
    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)
