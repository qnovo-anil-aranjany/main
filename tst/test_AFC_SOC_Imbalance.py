"""Test Module Description:
    Test module for 'AFC_LogSocImbalanceEvent' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_LogSocImbalanceEvent'
    functions for the fast charging algorithm works as expected under various scenarios.

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
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 255,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "cell_id": 1,
                },
                "Expected": {
                    "cycle_count": 255,
                    "cell_id": 1,
                },
            },
            id="test_case_log_soc_ombalance_1",
            marks=[
                mark.description(
                    "This test case check for soc imbalance buffer handle for initial test cell_id 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 5,
                    "cell_id": 2,
                },
                "Expected": {
                    "cycle_count": 2,
                    "cell_id": 2,
                },
            },
            id="test_case_log_soc_ombalance_2",
            marks=[
                mark.description(
                    "This test case check for soc imbalance buffer handle for initial test cell_id 2"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 10,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 14,
                    "cell_id": 3,
                },
                "Expected": {
                    "cycle_count": 10,
                    "cell_id": 3,
                },
            },
            id="test_case_log_soc_ombalance_3",
            marks=[
                mark.description(
                    "This test case check for soc imbalance buffer handle for initial test cell_id 3"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 100,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 14,
                    "cell_id": 4,
                },
                "Expected": {
                    "cycle_count": 100,
                    "cell_id": 4,
                },
            },
            id="test_case_log_soc_ombalance_4",
            marks=[
                mark.description(
                    "This test case check for soc imbalance buffer handle for initial test cell_id 4"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 110,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 0,
                    "cell_id": 5,
                },
                "Expected": {
                    "cycle_count": 110,
                    "cell_id": 5,
                },
            },
            id="test_case_log_soc_ombalance_5",
            marks=[
                mark.description(
                    "This test case check for soc imbalance buffer handle for initial test cell_id 5"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 316,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "cell_id": 6,
                },
                "Expected": {
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "cycle_count": 316,
                    "cell_id": 6,
                },
            },
            id="test_case_log_soc_ombalance_6",
            marks=[
                mark.description(
                    "This test case check for soc imbalance buffer handle for initial test cell_id 6"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 65535,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "cell_id": 191,
                },
                "Expected": {
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "cycle_count": 65535,
                    "cell_id": 191,
                },
            },
            id="test_case_log_soc_ombalance_7",
            marks=[
                mark.description(
                    "This test case check for soc imbalance buffer handle for initial test cell_id 191"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 65536,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "cell_id": 191,
                },
                "Expected": {
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "cycle_count": 65535,
                    "cell_id": 191,
                },
            },
            id="test_case_log_soc_ombalance_8",
            marks=[
                mark.description("This test case check for overflow error"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-429

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_LogSocImbalanceEvent from afc binary via cffi using input param cell_volts_temp,\
        Step4: compare output with expected value from input param - expected_indexes, corr_incr_val,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_LogCorrIdxEvent

        parent_suite: swc_fast_charge
        suite: afc_log_soc_imbalance_event
        sub_suite: log_soc_imbalance_event
        label: Unit / Integration
    """
)
def test_AFC_Log_SOC_Imbalance_event(lib, setup_parameters, test_cases) -> None:
    """
    Verify SOC imbalance is correctly logged.
    """
    try:
        set_lib_inputs(lib, test_cases)
        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )

        if "test_cell_values" in test_cases["Inputs"]:
            for item in test_cases["Inputs"]["test_cell_values"]:
                i, j, k = item
                if j != -1:
                    lib.cell_volts_temp[i] = j
                lib.SHR_InpHandle.Va_T_TempSnsrs[
                    lib.INP_Snsr.Ka_i_SeriesCell2TempIdx[i]
                ] = k
        else:
            logger.error("Provide test_cell_values for test")

        # logging event call method AFC_LogSocImbalanceEvent
        lib.AFC_LogSocImbalanceEvent(test_cases["Inputs"]["cell_id"])

        ele_addr = ffi.new("uint8_t [3]")
        obj = ffi.addressof(
            lib.AFC_LoggingTrack[0], "Ne_Afc_Soc_Imbalance_Logging_Circ_Buff_Handle"
        )
        num_elements_inserted = ffi.new("uint16_t *")
        lib.LIB_CircBuffNumElementsInserted(obj, num_elements_inserted)
        logger.debug(f"Elements Inserted: {num_elements_inserted[0]}")

        # Get recent inserted element
        lib.LIB_CircBuffGetElement(obj, 0, ele_addr)

        py_list = ffi.unpack(ele_addr, 3)
        actual_cycle_count = int.from_bytes(
            bytes(py_list[:2]), byteorder="little", signed=False
        )
        logger.info(f"Actual Cycle Count logged: {actual_cycle_count}")
        expected_cycle_id = test_cases["Expected"]["cycle_count"]
        compare_result(expected_cycle_id, actual_cycle_count)

        actual_cell_id = int.from_bytes(
            bytes(py_list[2:]), byteorder="little", signed=False
        )
        logger.info(f"Actual cell_id logged: {actual_cell_id}")
        expected_cell_id = test_cases["Expected"]["cell_id"]
        compare_result(expected_cell_id, actual_cell_id)

    except OverflowError:
        logger.error("An overflow of assigned variable occurred")
    else:
        pass
