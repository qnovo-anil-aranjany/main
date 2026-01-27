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

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


ffi = cffi.FFI()
_NVM_ARRAY_SIZE = 3750
_NUM_CELL = 192
_NUM_TEMP_SNSR = 18


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "VaAPI_Cmp_NVMRegion": [0] * _NVM_ARRAY_SIZE,
                    "VeAPI_I_PackCurr": 50000,
                    "VeAPI_b_PackCurr_DR": 1,
                    "VaAPI_U_SEVolts": [3200] * _NUM_CELL,
                    "VaAPI_b_SEVolts_DR": [1] * _NUM_CELL,
                    "VaAPI_T_TempSnsrs": [350] * _NUM_TEMP_SNSR,
                    "VaAPI_b_TempSnsrs_DR": [1] * _NUM_TEMP_SNSR,
                    "VeAPI_T_MinTempSnsr": 350,
                    "VeAPI_b_MinTempSnsr_DR": 1,
                    "VeAPI_T_MaxTempSnsr": 350,
                    "VeAPI_b_MaxTempSnsr_DR": 1,
                    "VeAPI_Cap_ChgPackCapcty": 16000,
                    "VeAPI_b_ChgPackCapcty_DR": 1,
                    "VeAPI_Pct_PackSOC": 5000,
                    "VeAPI_b_PackSOC_DR": 1,
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_e_EVSEChgLevel": 2,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 9,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [0] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 251000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_1_MainInit",
            marks=[
                mark.description("t=0s, Run MainInit"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 5000,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 9,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [0] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 251000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_2_MainPrdc",
            marks=[
                mark.description("t=1s, Run MainPrdc"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VaAPI_U_SEVolts": [4000] * _NUM_CELL,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 10,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [1] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 64,
                    "VeAFC_I_ChgPackCurr": 242000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_3_OverCPVLimit",
            marks=[
                mark.description(
                    "t=2s, enable tracking by being near 1% from end of stage"
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VaAPI_U_SEVolts": [4000] * _NUM_CELL,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 10,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [0] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 232000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_4_StartingNewStage",
            marks=[
                mark.description("t=3s, start a new stage"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 5740 - 50,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 10,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [0] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 232000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_5_TrackingEnabled",
            marks=[
                mark.description(
                    "t=4s, enable tracking by being near 1% from end of stage"
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 5741,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [1] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 232000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_6_EnterNewStageAttemptIncCPVIdx",
            marks=[
                mark.description("t=5s, attempt to increment CPV index"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 5741,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [0] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 214000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_7_ContinueInNewStage",
            marks=[
                mark.description("t=6s, continue with the new stage post attempt"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_b_EVSEChgStatus": 0,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [0] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 0,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_8_Reset Charging Status",
            marks=[
                mark.description("t=7s, set charging status to 0"),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_Pct_PackSOC": 5000,
                    "VaAPI_U_SEVolts": [3200] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 9,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [0] * _NUM_CELL,
                    "VeAFC_e_WarningFlags": 0,
                    "VeAFC_I_ChgPackCurr": 251000,
                    "VeAFC_U_ChgPackVolt": 816000,
                },
            },
            id="Test_Case_9_RepeatEverything",
            marks=[
                mark.description("t=8s, Repeat as if test case 1 again"),
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
        Step3: Invoke method Qnovo_AFC_1000ms from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - sAFC_Calc.Ve_Cnt_PresentStgNum \
        Va_Cnt_CPVCorrIdx, VeAFC_e_WarningFlags, VeAFC_I_ChgPackCurr, VeAFC_U_ChgPackVolt,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: qnovo_afc_api.c
        Method_In_Test: Qnovo_AFC

        parent_suite: swc_fast_charge
        suite: afc_1000ms_worst_case_path
        sub_suite: 1000ms_worst_case_path
    """
)
def test_Qnovo_AFC_1000ms_WorstCasePath(lib, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_MainPrdc' function.
    """

    # Setup Variables
    # ------------------------------------------------
    lib.INP_Snsr.Ke_n_NumCellSeries = 192
    lib.AFC_Param.Ka_U_Stg_RefStartSEVolt[9] = 3000
    lib.AFC_Param.Ka_U_Stg_RefStartSEVolt[10] = 3700
    lib.AFC_Param.Ka_U_Stg_SADCellLim[9] = 3340
    set_lib_inputs(lib, test_cases)

    if lib.VeAPI_b_EVSEChgStatus == 0:
        size_row, size_col = size(lib.AFC_Track.Nt_Cnt_CPVCorrIdx)
        lib.AFC_Track.Nt_Cnt_CPVCorrIdx = [[0] * size_col for _ in range(size_row)]

        size_row, size_col = size(lib.AFC_Track.Nt_U_RefSEVolt)
        lib.AFC_Track.Nt_U_RefSEVolt = [[0] * size_col for _ in range(size_row)]

    # Run Function
    # ------------------------------------------------
    lib.Qnovo_AFC(ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs"))

    # Use these lines for updating testrail when required
    # log_for_testrail_update("Qnovo_AFC")
    logger.info(
        f"ACTUAL: AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
        f"AFC_Calc.Va_Cnt_CPVCorrIdx={lib.AFC_Calc.Va_Cnt_CPVCorrIdx},"
        f"VeAFC_e_WarningFlags={lib.VeAFC_e_WarningFlags},"
        f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr},"
        f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt}"
    )
    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)
