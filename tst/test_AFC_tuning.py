"""Test Module Description:
    Test module for 'Tuning' function in the fast charging algorithm.

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
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 0,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for default tuning flag",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 1,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_2",
            marks=[
                mark.description(
                    "This test case check for default tuning flag",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 2,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.08,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_3",
            marks=[
                mark.description(
                    "This test case check for default tuning flag",
                ),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-487, QAFC-485, 

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_LogCorrIdxEvent from afc binary via cffi using input param stage and cycle,\
        Step4: compare output with expected value from input param - expected_indexes, corr_incr_val,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_Tuning

        parent_suite: swc_fast_charge
        suite: afc_set_tuning
        sub_suite: check_tuning_flag
        label: Unit / Integration
    """
)
def test_AFC_Tuning(lib, setup_parameters, test_cases) -> None:
    """
    Test cases of AFC tuning functionality verification
    """
    try:
        set_lib_inputs(lib, test_cases)
        logger.info(lib.VeAPI_e_TuningState)
        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        lib.Qnovo_AFC(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        actual = lib.AFC_HiTempDerate.Ke_k_Alpha
        expected = test_cases["Expected"]["alpha"]
        compare_result(expected, actual, rtol=1e-2)

    except OverflowError:
        logger.error("An overflow of assigned variable occurred")
    else:
        pass


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 1,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 0,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 0, tuning state 0, we get default tuning.",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_2",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 0, tuning state 1, we get new tuning.",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.06,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_3",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 1, tuning state 1, we get existing tuning."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.06,
                },
                "Expected": {
                    "alpha": 1.06,
                },
            },
            id="test_case_tuning_4",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 0, tuning state 1, we get new tuning."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 0,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.06,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_5",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 0, tuning state 0, we get default tuning."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 2,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.06,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_6",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 0, tuning state 1, we get new tuning."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.04,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_7",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 1, tuning state 1, we get existing tuning."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 2,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_8",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 1, tuning state 1, we get existing tuning."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.03,
                },
                "Expected": {
                    "alpha": 1.03,
                },
            },
            id="test_case_tuning_9",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 0, tuning state 1, we get new tuning."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 390,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.03,
                },
                "Expected": {
                    "alpha": 1.03,
                },
            },
            id="test_case_tuning_10",
            marks=[
                mark.description(
                    "This test case check for tuning when charge status is 0, tuning state 1,"
                    "VeAPI_e_Tbgn < AFC_HIGH_TEMP_DERATE_BEGIN_TEMP_LO_LIM. Should not accept tuning"
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.08,
                },
                "Expected": {
                    "alpha": 1.08,
                },
            },
            id="test_case_tuning_11",
            marks=[
                mark.description(
                    "Good for Tuning Unlock, values set and stored in NVM."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 511,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.03,
                },
                "Expected": {
                    "alpha": 1.08,
                },
            },
            id="test_case_tuning_12",
            marks=[
                mark.description(
                    "VeAPI_e_Tbgn > AFC_HIGH_TEMP_DERATE_BEGIN_TEMP_HI_LIM for Tuning Unlock,"
                    "values rejected and tuning state 0."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.04,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_13",
            marks=[
                mark.description(
                    "Good for Tuning Unlock, values set and stored in NVM."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 499,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_14",
            marks=[
                mark.description(
                    "VeAPI_e_Tlim < AFC_HIGH_TEMP_DERATE_LIMIT_TEMP_LO_LIM Good for Tuning Unlock,"
                    "values rejected."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 0.49,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_15",
            marks=[
                mark.description(
                    "VeAPI_e_Ab < AFC_HIGH_TEMP_DERATE_ABRUPTNESS_LO_LIM for Tuning Unlock,"
                    "values rejected."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 4.01,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_16",
            marks=[
                mark.description(
                    "VeAPI_e_Ab > AFC_HIGH_TEMP_DERATE_ABRUPTNESS_HI_LIM for Tuning Unlock,"
                    "values rejected."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 0.9,
                    "VeAPI_e_Dp": -0.1,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_17",
            marks=[
                mark.description(
                    "VeAPI_e_Dp < AFC_HIGH_TEMP_DERATE_DISPERSITY_LO_LIM for Tuning Unlock,"
                    "values rejected."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 0.9,
                    "VeAPI_e_Dp": 3.1,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_18",
            marks=[
                mark.description(
                    "VeAPI_e_Dp > AFC_HIGH_TEMP_DERATE_DISPERSITY_HI_LIM for Tuning Unlock,"
                    "values rejected."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 0.9,
                    "VeAPI_e_Dp": 2.1,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 0,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_19",
            marks=[
                mark.description(
                    "VeAPI_e_Alpha < AFC_TUNING_PARAM_ALPHA_LO_LIM for Tuning Unlock,"
                    "values rejected."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "AFC_Track.Ne_Cnt_ChargeCycleNum": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 1,
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 0.9,
                    "VeAPI_e_Dp": 2.1,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.09,
                },
                "Expected": {
                    "alpha": 1.04,
                },
            },
            id="test_case_tuning_20",
            marks=[
                mark.description(
                    "VeAPI_e_Alpha > AFC_TUNING_PARAM_ALPHA_HI_LIM for Tuning Unlock,"
                    "values rejected."
                ),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-314

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_LogCorrIdxEvent from afc binary via cffi using input param stage and cycle,\
        Step4: compare output with expected value from input param - expected_indexes, corr_incr_val,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_Tuning

        parent_suite: swc_fast_charge
        suite: afc_set_tuning
        sub_suite: check_tuning_coverage
    """
)
def test_AFC_Tuning_coverage(lib, setup_parameters, test_cases) -> None:
    """
    Tuning coverage test cases for code coverage
    """
    try:
        set_lib_inputs(lib, test_cases)
        logger.info(lib.VeAPI_e_TuningState)
        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        lib.Qnovo_AFC(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        actual = lib.AFC_HiTempDerate.Ke_k_Alpha
        expected = test_cases["Expected"]["alpha"]
        compare_result(expected, actual, rtol=1e-2)

    except OverflowError:
        logger.error("An overflow of assigned variable occurred")
    else:
        pass
