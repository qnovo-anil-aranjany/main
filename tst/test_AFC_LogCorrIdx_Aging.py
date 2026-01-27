"""Test Module Description:
    Test module for 'AFC_LogCorrIdxEvent' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_LogCorrIdxEvent'
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


def get_set_bit_positions(number):
    """
    Returns a list of positions of set bits in the binary representation of a number.
    Positions are 0-indexed from the right (least significant bit).
    """
    if number < 0:
        raise ValueError("Input number must be non-negative.")
    positions = []
    index = 0
    temp_number = number
    while temp_number > 0:
        # Check if the rightmost bit is set
        if (temp_number & 1) == 1:
            positions.append(index)
        # Right shift the number to check the next bit
        temp_number >>= 1
        index += 1
    return positions


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, 1, 1],
                        [3, 1, -32768],
                        [23, 1, -13108],
                        [100, 1, 13107],
                        [189, 1, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "highest_index": 0,
                },
                "Expected": {
                    "expected_indexes": [189, 100, 73, 23, 3],
                    "corr_incr_val": 1,
                    "cycle_count": 0,
                    "stage": 1,
                    "expected_temp": [-4377, 13107, 1, -13108, -32768],
                    "expected_warnings": [],
                    "nvm_warnings": [],
                    "highest_index": 0,
                },
            },
            id="test_case_log_aging_1",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for initial test"
                    "SAD value is 1, volt value is 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 0,
                    "test_cell_values": [
                        [73, 1, 1],
                        [3, 1, -32768],
                        [23, 1, -13108],
                        [100, 1, 13107],
                        [189, 1, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 5,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 5,
                    "highest_index": 14,
                },
                "Expected": {
                    "expected_indexes": [189, 100, 73, 23, 3],
                    "corr_incr_val": 0,
                    "cycle_count": 5,
                    "stage": 5,
                    "expected_temp": [-4377, 13107, 1, -13108, -32768],
                    "expected_warnings": [],
                    "nvm_warnings": [],
                    "highest_index": 14,
                },
            },
            id="test_case_log_aging_2",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for second test"
                    "SAD value is 0, volt value is 1"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 0,
                    "test_cell_values": [
                        [73, 0, 1],
                        [3, 0, -32768],
                        [23, 0, -13108],
                        [100, 0, 13107],
                        [189, 0, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 70,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 14,
                    "highest_index": 13,
                },
                "Expected": {
                    "expected_indexes": [191, 190, 189, 188, 187],
                    "corr_incr_val": 0,
                    "cycle_count": 70,
                    "stage": 14,
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "expected_warnings": [],
                    "nvm_warnings": [],
                    "highest_index": 13,
                },
            },
            id="test_case_log_aging_3",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for third test"
                    "SAD value is 0, volt value is 0"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, 10, 1],
                        [3, 109, -32768],
                        [23, 745, -13108],
                        [100, 1300, 13107],
                        [189, 3000, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 80,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 14,
                    "highest_index": 8,
                },
                "Expected": {
                    "expected_indexes": [189, 100, 23, 3, 73],
                    "corr_incr_val": 1,
                    "cycle_count": 80,
                    "stage": 14,
                    "expected_temp": [-4377, 13107, -13108, -32768, 1],
                    "expected_warnings": [12],
                    "nvm_warnings": ["normal"],
                    "highest_index": 8,
                },
            },
            id="test_case_log_aging_4",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for fourth test"
                    "SAD value is 1, volt value is varies"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, 1000, 1],
                        [3, 1000, -32768],
                        [23, 1000, -13108],
                        [100, 1000, 13107],
                        [189, 1000, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 82,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 0,
                    "highest_index": 9,
                },
                "Expected": {
                    "expected_indexes": [189, 100, 73, 23, 3],
                    "corr_incr_val": 1,
                    "cycle_count": 82,
                    "stage": 0,
                    "expected_temp": [-4377, 13107, 1, -13108, -32768],
                    "expected_warnings": [12],
                    "nvm_warnings": ["abnormal"],
                    "highest_index": 9,
                },
            },
            id="test_case_log_aging_5",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for fifth test"
                    "SAD value is 1, volt value is same for 5 cells"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, -1, 1],
                        [3, -1, -32768],
                        [23, -1, -13108],
                        [100, -1, 13107],
                        [189, -1, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 316,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 11,
                    "highest_index": 10,
                },
                "Expected": {
                    "expected_indexes": [191, 190, 189, 188, 187],
                    "corr_incr_val": 1,
                    "cycle_count": 316,
                    "stage": 11,
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "expected_warnings": [12],
                    "nvm_warnings": ["abnormal"],
                    "highest_index": 10,
                },
            },
            id="test_case_log_aging_6",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for fourth insertion"
                    "SAD value is 1, volt value is defau;t for all cells (0)"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, -1, 1],
                        [3, -1, -32768],
                        [23, -1, -13108],
                        [100, -1, 13107],
                        [189, -1, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 317,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "highest_index": 1,
                },
                "Expected": {
                    "expected_indexes": [191, 190, 189, 188, 187],
                    "corr_incr_val": 1,
                    "cycle_count": 317,
                    "stage": 12,
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "expected_warnings": [12],
                    "nvm_warnings": ["abnormal"],
                    "highest_index": 1,
                },
            },
            id="test_case_log_aging_7",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for fourth insertion"
                    "SAD value is 1, volt value is defau;t for all cells (0)"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, -1, 1],
                        [3, -1, -32768],
                        [23, -1, -13108],
                        [100, -1, 13107],
                        [189, -1, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 318,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 13,
                    "highest_index": 14,
                },
                "Expected": {
                    "expected_indexes": [191, 190, 189, 188, 187],
                    "corr_incr_val": 1,
                    "cycle_count": 318,
                    "stage": 13,
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "expected_warnings": [12],
                    "nvm_warnings": ["abnormal"],
                    "highest_index": 14,
                },
            },
            id="test_case_log_aging_8",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for fourth insertion"
                    "SAD value is 1, volt value is defau;t for all cells (0)"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, -1, 1],
                        [3, -1, -32768],
                        [23, -1, -13108],
                        [100, -1, 13107],
                        [189, -1, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 319,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 14,
                    "highest_index": 11,
                },
                "Expected": {
                    "expected_indexes": [191, 190, 189, 188, 187],
                    "corr_incr_val": 1,
                    "cycle_count": 319,
                    "stage": 14,
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "expected_warnings": [12, 13],
                    "nvm_warnings": ["abnormal", "extreme"],
                    "highest_index": 11,
                },
            },
            id="test_case_log_aging_9",
            marks=[
                mark.description(
                    "This test case check for log buffer handle for fourth insertion"
                    "SAD value is 1, volt value is defau;t for all cells (0)"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "cell_volts_temp": [np.uint16(0) for _ in range(192)],
                    "ele_addr": ffi.new("uint8_t [18]"),
                    "corr_incr_val": 1,
                    "test_cell_values": [
                        [73, -1, 1],
                        [3, -1, -32768],
                        [23, -1, -13108],
                        [100, -1, 13107],
                        [189, -1, -4377],
                    ],
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 320,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 15,
                    "highest_index": 5,
                },
                "Expected": {
                    "expected_indexes": [191, 190, 189, 188, 187],
                    "corr_incr_val": 1,
                    "cycle_count": 320,
                    "stage": 15,
                    "expected_temp": [-4377, -4377, -4377, -4377, -4377],
                    "expected_warnings": [12, 13],
                    "nvm_warnings": ["abnormal", "extreme"],
                    "highest_index": 5,
                },
            },
            id="test_case_log_aging_10",
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
        JIRA-ID: QAFC-299, QAFC-423, QAFC-414, QAFC-397, , QAFC-419, 

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_LogCorrIdxEvent from afc binary via cffi using input param cell_volts_temp,\
        Step4: compare output with expected value from input param - expected_indexes, corr_incr_val,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_LogCorrIdxEvent

        parent_suite: swc_fast_charge
        suite: afc_log_corridx_aging
        sub_suite: log_corridx_check_aging
        label: Unit / Integration
    """
)
def test_AFC_LogCorrIdxEvent_check_aging(lib, setup_parameters, test_cases) -> None:
    """
    Verify logging of cell aging events correctly into the log buffer.
    """
    try:
        set_lib_inputs(lib, test_cases)

        lib.AFC_Track.Na_Cnt_HighestCPVCorrIdx[lib.AFC_Calc.Ve_Cnt_PresentStgNum] = (
            test_cases
        )["Inputs"]["highest_index"]
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

        # logging event call method AFC_LogCorrIdxEvent
        lib.AFC_LogCorrIdxEvent(list(lib.cell_volts_temp))

        logger.debug(f"Warning Flag: {lib.VeAFC_e_WarningFlags}")
        warning_set = get_set_bit_positions(lib.VeAFC_e_WarningFlags)
        logger.debug(f"Binary : {warning_set}")

        # check AFC Track for warnings:
        if "normal" in test_cases["Expected"]["nvm_warnings"]:
            assert (True, lib.AFC_Outputs.EarlyWarningAgingFlag)
        else:
            assert (False, lib.AFC_Outputs.EarlyWarningAgingFlag)
        if "abnormal" in test_cases["Expected"]["nvm_warnings"]:
            assert (True, lib.AFC_Outputs.AbnormalAgingFlag)
        else:
            assert (False, lib.AFC_Outputs.AbnormalAgingFlag)
        if "extreme" in test_cases["Expected"]["nvm_warnings"]:
            assert (True, lib.AFC_Outputs.ExtremeAgingFlag)
        else:
            assert (False, lib.AFC_Outputs.ExtremeAgingFlag)

        logger.info(lib.AFC_Outputs.EarlyWarningAgingFlag[0])
        logger.info(lib.AFC_Outputs.AbnormalAgingFlag[0])
        logger.info(lib.AFC_Outputs.ExtremeAgingFlag[0])
        # for debug purpose log the warning
        try:
            for item in warning_set:
                warning_set_string = warning_map[item + 1]
                logger.debug(f"Warning Set: {warning_set_string}")

        except KeyError:
            logger.error(
                f"Warning flag for key : {lib.VeAFC_e_WarningFlags} do not exist"
            )

        obj = ffi.addressof(lib.AFC_LoggingTrack[0], "Ne_Afc_Logging_Circ_Buff_Handle")
        logger.info(f"Elements Inserted: {get_num_elements_from_buffer(lib)}")
        # Parse log buffer and get result data
        result = process_log_buffer(lib)
        result.print_buffer()

        # Get and compare indexes logged with expected result
        expected_indexes = test_cases["Expected"]["expected_indexes"]
        compare_result(expected_indexes, result.indexes)
        expected_cycle_count = test_cases["Expected"]["cycle_count"]
        compare_result(expected_cycle_count, result.cycle_count)
        expected_stage = test_cases["Expected"]["stage"]
        compare_result(expected_stage, result.stage)
        expected_temp = test_cases["Expected"]["expected_temp"]
        compare_result(expected_temp, result.temperatures)
        expected_highest_index = test_cases["Expected"]["highest_index"]
        compare_result(expected_highest_index, result.highest_index)
    except OverflowError:
        logger.error("An overflow of assigned variable occurred")
