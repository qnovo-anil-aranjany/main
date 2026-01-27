"""Test Module Description:
    Test module for 'AFC_UpdateNvmRestCmdForNextPwrCycle' function in the fast charging algorithm.

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


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 1,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm reset setting reset flag",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 2,
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 0,
                    "afc_init": True,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm after reset flag in effect",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 2,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 0,
                    "afc_init": True,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm after reset 0, tuning LOCK",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 0,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm after reset 0, tuning Unlock. previous NVM (which is saved in"
                    "previous call is in effect",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 0,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 1,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm after reset 0, tuning Unlock. previous NVM (which is saved in"
                    "previous call is in effect",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 0,
                    "afc_init": True,
                },
                "Expected": {
                    "alpha": 1.0,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm reset issued. previous NVM (which is saved in"
                    "previous call is in effect",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 0,
                    "afc_init": True,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm after reset, default is alpha",
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_e_TuningState": 1,
                    "VeAPI_b_EVSEChgStatus": 1,
                    "VeAPI_e_Ab": 1.2,
                    "VeAPI_e_Dp": 1.5,
                    "VeAPI_e_Tbgn": 490,
                    "VeAPI_e_Tlim": 560,
                    "VeAPI_e_Alpha": 1.02,
                    "VeAPI_e_NVMReset": 0,
                },
                "Expected": {
                    "alpha": 1.02,
                },
            },
            id="test_case_tuning_1",
            marks=[
                mark.description(
                    "This test case check for nvm after reset, default is alpha",
                ),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-490

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
        sub_suite: nvm_reset_coverage
        label: Unit / Integration
    """
)
def test_AFC_NVMreset_coverage(lib, setup_parameters, test_cases) -> None:
    """
    Verify the functionality for NVM_RESET work as expected when reset flag is True.
    """
    try:
        set_lib_inputs(lib, test_cases)
        logger.debug("\n1 Next Test NVM Reset 1, Tuning state 1\n")

        if (
            "afc_init" in test_cases["Inputs"]
            and test_cases["Inputs"]["afc_init"] is True
        ):
            lib.Qnovo_AFC_Init()

        lib.Qnovo_AFC(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )
        logger.debug(
            f"\nAfter reset AFC_HiTempDerate.Ke_k_Alpha: {lib.AFC_HiTempDerate.Ke_k_Alpha}"
        )
        logger.debug(f"\nAfter reset AFC Track: {lib.AFC_Track.Ne_k_Alpha}")
        expected = test_cases["Expected"]["alpha"]
        actual = lib.AFC_HiTempDerate.Ke_k_Alpha
        compare_result(expected, actual, rtol=1e-2)

    except OverflowError:
        logger.error("An overflow of assigned variable occurred")
    else:
        pass
