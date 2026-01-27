"""Test Module Description:
    Test module for verifying EOL condition via unit test in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_MainPrdc'
    functions for the fast charging algorithm calculate EOL status.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""

from .main import *

ffi = cffi.FFI()
MAKE_HTML = True
TOTAL_BYTES = 18

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
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "highest_index": 60,
                },
                "Expected": {
                    "highest_index": 60,
                    "total_mitigations": 60,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_1",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 60, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 5,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 5,
                    "highest_index": 54,
                },
                "Expected": {
                    "highest_index": 54,
                    "total_mitigations": 114,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_2",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 114, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 10,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 14,
                    "highest_index": 62,
                },
                "Expected": {
                    "highest_index": 62,
                    "total_mitigations": 174,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_3",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 174, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 15,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 17,
                    "highest_index": 60,
                },
                "Expected": {
                    "highest_index": 60,
                    "total_mitigations": 234,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_4",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 234, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 20,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 3,
                    "highest_index": 59,
                },
                "Expected": {
                    "highest_index": 59,
                    "total_mitigations": 293,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_5",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 293, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 316,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "highest_index": 60,
                },
                "Expected": {
                    "highest_index": 60,
                    "total_mitigations": 353,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_6",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 353, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 317,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "highest_index": 50,
                },
                "Expected": {
                    "highest_index": 50,
                    "total_mitigations": 403,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_7",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 403, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 318,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 10,
                    "highest_index": 58,
                },
                "Expected": {
                    "highest_index": 58,
                    "total_mitigations": 461,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_8",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 461, eol status is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 319,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 8,
                    "highest_index": 61,
                },
                "Expected": {
                    "highest_index": 61,
                    "total_mitigations": 522,
                    "eol_status": 0,
                },
            },
            id="test_case_logcorridxevent_9",
            marks=[
                mark.description(
                    "This test case check for eol (end of life) status for total mitigations 6522, eol status is 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 320,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 4,
                    "highest_index": 1,
                },
                "Expected": {
                    "highest_index": 1,
                    "total_mitigations": 523,
                    "eol_status": 1,
                },
            },
            id="test_case_logcorridxevent_10",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for fourth insertion"
                    "SAD value is 1, volt value is defau;t for all cells (0)"
                ),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-299, QAFC-432

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_MainPrdc from afc binary via cffi using input param cell_volts_temp,highest_index\
        Step4: compare output with expected value from input param - eol_status\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_LogCorrIdxEvent

        parent_suite: swc_fast_charge
        suite: afc_log_corridx_event
        sub_suite: log_corridx_event_check_eol
    """
)
def test_AFC_logCorrIdxEvent_eol_check(lib, setup_parameters, test_cases) -> None:
    """
    Check for EOL warnings for logging, when charge cycle reach expected life term.
    """
    try:
        set_lib_inputs(lib, test_cases)

        lib.AFC_Track.Na_Cnt_HighestCPVCorrIdx[lib.AFC_Calc.Ve_Cnt_PresentStgNum] = (
            test_cases
        )["Inputs"]["highest_index"]
        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        lib.AFC_MainPrdc(False)
        logger.info(f"EOL Flag : {lib.AFC_Track.Ne_b_EOLFlag}")

        expected_eol_flag = test_cases["Expected"]["eol_status"]
        actual_eol_flag = lib.AFC_Track.Ne_b_EOLFlag
        compare_result(expected_eol_flag, actual_eol_flag)
    except OverflowError:
        logger.error("An overflow of assigned variable occurred")
