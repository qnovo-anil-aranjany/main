"""Test Module Description:
    Test module for 'LIB_LogData' function in the shared common libraries.

    This test group contains pytest test cases designed to ensure that the 'LIB_LogData'
    functions in the fast charging algorithm works as expected under various scenarios.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""

from .main import *

ffi = cffi.FFI()
XOR_KEY = 0xBD
CombineObfuscate = 3

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

RUN_STACK_PARAM_TESTS = False  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = True  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)

if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {"VeAPI_Cmp_LogSrc": 10484130},
                "Expected": {"VeAPI_Cmp_LogDst": 10484130},
            },
            id="Test_Case_1",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is -1.0 celsius."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"VeAPI_Cmp_LogSrcArray": [6] * 100},
                "Expected": {"VeAPI_Cmp_LogDstArray": [6] * 100},
            },
            id="Test_Case_1",
            marks=[
                mark.description(
                    "This checks current compensation when Cell temperature is -1.0 celsius."
                ),
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
        Step3: Invoke method LIB_LogData and LIB_Deobfuscate from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - VeAPI_cmp_LogDstArray,\
        Step5: Test result should match with expected value,\

        Source_File_In_Test: lib_common_utils.c
        Method_In_Test: LIB_Deobfuscate

        parent_suite: swc_fast_charge
        suite: afc_lib_log_obfuscation
        sub_suite: lib_log_obfuscation
    """
)
def test_LIB_LogData(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'LIB_LogData'
    function.
    """

    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    # Run Function
    # ------------------------------------------------
    lib.LIB_LogData(
        ffi.addressof(lib, "VeAPI_Cmp_LogDst"),
        ffi.addressof(lib, "VeAPI_Cmp_LogSrc"),
        lib.VeAPI_Cmp_LogSrcSize,
        CombineObfuscate,
    )

    lib.LIB_Deobfuscate(
        ffi.addressof(lib, "VeAPI_Cmp_LogDst"), lib.VeAPI_Cmp_LogSrcSize, XOR_KEY
    )

    lib.LIB_LogData(
        ffi.addressof(lib, "VeAPI_Cmp_LogDstArray"),
        ffi.addressof(lib, "VeAPI_Cmp_LogSrcArray"),
        lib.VeAPI_Cmp_LogSrcArraySize,
        CombineObfuscate,
    )

    lib.LIB_Deobfuscate(
        ffi.addressof(lib, "VeAPI_Cmp_LogDstArray"),
        lib.VeAPI_Cmp_LogSrcArraySize,
        XOR_KEY,
    )

    # Use these lines for updating testrail when required
    # log_for_testrail_update("LIB_Deobfuscate")
    logger.info(f"ACTUAL: VeAPI_Cmp_LogDstArray={lib.VeAPI_Cmp_LogDstArray}")
    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)
