"""Test Module Description:
    Test module for 'AFC_KeepTrackOfChrgCycles' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_KeepTrackOfChrgCycles'
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


if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 0,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 0,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                },
            },
            id="test_case_track_chargecycle_1",
            marks=[
                mark.description(
                    "This test case check for first time setting for Ne_Cnt_SocIncrAccum,"
                    "which is 0 with current implementation logic"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 1000,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 1000,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                },
            },
            id="test_case_track_chargecycle_2",
            marks=[
                mark.description(
                    "This test case check for second time setting for Ne_Cnt_SocIncrAccum,"
                    "which is an increment from previous with current implementation logic for 1000,"
                    "current_soc > previous_soc, soc_increment = current_soc - previous_soc, and soc_increment < 10K"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 10000,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 0,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 1,
                },
            },
            id="test_case_track_chargecycle_3",
            marks=[
                mark.description(
                    "This test case check Ne_Cnt_SocIncrAccum reaching 100%,"
                    "where Ne_Cnt_SocIncrAccum is set back to 0 and charge cycle is incremented by 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 10,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 0,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 1,
                },
            },
            id="test_case_track_chargecycle_4",
            marks=[
                mark.description(
                    "This test case check Ne_Cnt_SocIncrAccum reaching 10% for next charging,"
                    "At this point previous_soc is 10K, and in algorithm we just set the previous soc to current soc"
                    "no other changes to other data points"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 15,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 5,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 1,
                },
            },
            id="test_case_track_chargecycle_5",
            marks=[
                mark.description(
                    "This test case check Ne_Cnt_SocIncrAccum reaching 15%%,"
                    "where Ne_Cnt_SocIncrAccum is current_soc - previous_soc(15-10), and charge cycle is same as 1"
                    "previous_soc is set to 15 (current_soc)"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 10000,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 9990,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 1,
                },
            },
            id="test_case_track_chargecycle_6",
            marks=[
                mark.description(
                    "This test case check Ne_Cnt_SocIncrAccum reaching 100%,"
                    "where Ne_Cnt_SocIncrAccum is current_soc - previous_soc + Ne_Cnt_SocIncrAccum (10000 - 15 + 5),"
                    " previous_soc is set to 10K, and charge cycle is 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 100,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 9990,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 1,
                },
            },
            id="test_case_track_chargecycle_7",
            marks=[
                mark.description(
                    "This test case check Ne_Cnt_SocIncrAccum reaching 100%, previous_soc at this point is 10K"
                    "since current soc is 100, no changes other than setting previous_soc to 100 internally"
                    "where Ne_Cnt_SocIncrAccum is retained as 9990 and charge cycle is 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 200,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 90,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 2,
                },
            },
            id="test_case_track_chargecycle_8",
            marks=[
                mark.description(
                    "This test case check Ne_Cnt_SocIncrAccum reaching 100%, previous_soc at this point is 100"
                    "where Ne_Cnt_SocIncrAccum is Ne_Cnt_SocIncrAccum + (cur_soc - previous_soc): 9990 + 200 - 100"
                    "Ne_Cnt_SocIncrAccum > 10K so Ne_Cnt_SocIncrAccum is set to Ne_Cnt_SocIncrAccum - 10K"
                    "and charge cycle is incremented by 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 2000000,
                },
                "Expected": {
                    "AFC_Track.Ne_Cnt_SocIncrAccum": 90,
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 2,
                },
            },
            id="test_case_track_chargecycle_9",
            marks=[
                mark.description(
                    "This test case packsoc is already 100% There is no effect for Ne_Cnt_SocIncrAccum"
                    "charge cycle num is reatined as 2"
                ),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-299, QAFC-417, QAFC-409, QAFC-392, QAFC-381

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_CheckChgCompletion from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - VeAFC_b_ChgCompletionFlag, VeAFC_I_ChgPackCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_KeepTrackOfChrgCycles

        parent_suite: swc_fast_charge
        suite: afc_track_charge_cycles
        sub_suite: track_charge_cycles
    """
)
def test_AFC_TrackChargeCycles(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the
    'AFC_CheckChgCompletion' function.
    """

    # Setup Variables
    # ------------------------------------------------
    try:
        set_lib_inputs(lib, test_cases)

        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        logger.debug(f"Previous SOC: {lib.Le_Pct_Previous_SOC}")

        lib.AFC_KeepTrackOfChrgCycles(test_cases["Inputs"]["VeAPI_Pct_PackSOC"])
    except OverflowError:
        logger.error("An overflow of assigned variable occurred")
    else:
        logger.debug(
            f"lib.AFC_Track.Ne_Cnt_SocIncrAccum: {lib.AFC_Track.Ne_Cnt_SocIncrAccum}"
        )
        expected = test_cases["Expected"]["AFC_Track.Ne_Cnt_SocIncrAccum"]
        actual = lib.AFC_Track.Ne_Cnt_SocIncrAccum
        compare_result(expected, actual)

        expected = test_cases["Expected"]["AFC_Track.Ne_Cnt_ChargeCycleNum"]
        actual = lib.AFC_Track.Ne_Cnt_ChargeCycleNum
        compare_result(expected, actual)
        logger.debug(
            f"AFC_Track->Ne_Cnt_ChargeCycleNum: {lib.AFC_Track.Ne_Cnt_ChargeCycleNum}"
        )
