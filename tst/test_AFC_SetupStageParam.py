"""Test Module Description:
    Test module for 'AFC_SetupStageParam' function in the fast charging algorithm.

    This test group contains pytest test cases designed to ensure that the 'AFC_SetupStageParam'
    functions for the fast charging algorithm works as expected under various scenarios.

Requirements:
    - VCCFC-110
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""

from .main import *

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.
MAKE_HTML = True
RUN_STACK_PARAM_TESTS = True  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = True  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)
ffi = cffi.FFI()
if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {"VeAPI_Pct_PackSOC": 9601},
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 25,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3200] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 30000,
                },
            },
            id="Test_Case_1_ConstantVoltage",
            marks=[
                mark.description(
                    "This checks that the stage is not incremented under high SOC conditions (i.e. constant voltage "
                    "scenario)."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"VeAPI_Pct_PackSOC": 6370},
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 13,
                    "AFC_Calc.Va_b_ValidSampleFlag": [0] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [0] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 180000,
                },
            },
            id="Test_Case_2_IncrementStages",
            marks=[
                mark.description(
                    "This checks that under normal operating conditions, 'AFC_Calc.Ve_Cnt_PresentStgNum' is "
                    "incremented to the correct stage based on SOC."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"VeAPI_Pct_PackSOC": 8490},
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 22,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3200] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 72000,
                },
            },
            id="Test_Case_3_NotCPVStage",
            marks=[
                mark.description(
                    "This checks for when not in CPV condition, the function should not reset both "
                    "'AFC_Calc.Va_b_ValidSampleFlag' and 'AFC_Calc.Va_U_SampleSEVolt'."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "VeAPI_Pct_PackSOC": 0,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 26,
                },
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 26,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3200] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 30000,
                },
            },
            id="Test_Case_4_ExceedMaxStage",
            marks=[
                mark.description(
                    "This checks whether the function will further increment 'AFC_Calc.Ve_Cnt_PresentStgNum' in the edge case where it "
                    "has already surpassed the maximum stage."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {"VeAPI_Pct_PackSOC": 0},
                "Expected": {
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 0,
                    "AFC_Calc.Va_b_ValidSampleFlag": [0] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [0] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 345000,
                },
            },
            id="Test_Case_5_ZeroStage",
            marks=[
                mark.description(
                    "This checks whether the function increments 'AFC_Calc.Ve_Cnt_PresentStgNum' in the specific edge case where "
                    "both 'AFC_Calc.Ve_Cnt_PresentStgNum' and 'VeAPI_Pct_PackSOC' are zero."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        Steps:\
        Step1: StepHave the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        Step3: Invoke method AFC_SetupStageParam from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - sAFC_Calc.Ve_Cnt_PresentStgNum\
        Va_b_ValidSampleFlag, Va_U_SampleCellVolt, VeAFC_U_ChgPackVolt, VeAFC_I_ChgPackCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_SetupStageParam

        parent_suite: swc_fast_charge
        suite: afc_setup_stage_param
        sub_suite: setup_stage_param
    """
)
def test_AFC_SetupStageParam(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_SetupStageParam'
    function.
    """

    # Setup Variables
    # ------------------------------------------------
    lib.AFC_Calc.Va_b_ValidSampleFlag = [1] * size(lib.AFC_Calc.Va_b_ValidSampleFlag)
    lib.AFC_Calc.Va_U_SampleSEVolt = [3200] * size(lib.AFC_Calc.Va_U_SampleSEVolt)
    lib.AFC_Calc.Va_Cnt_CPVCorrIdx = [5] * size(lib.AFC_Calc.Va_Cnt_CPVCorrIdx)

    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    lib.AFC_SetupStageParam()

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_SetupStageParam")
    logger.info(
        f"ACTUAL: AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
        f"AFC_Calc.Va_b_ValidSampleFlag={lib.AFC_Calc.Va_b_ValidSampleFlag},"
        f"AFC_Calc.Va_U_SampleSEVolt={list(lib.AFC_Calc.Va_U_SampleSEVolt)},"
        f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt},"
        f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
    )
    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)


# =======================================================================
# Stack-Parametrize Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "VeAPI_Pct_PackSOC": [x for x in range(0, 10001, 2000)],
        "AFC_Calc.Ve_Cnt_PresentStgNum": [x for x in range(0, 27, 2)],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            Steps:\
            Step1: Have the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_SetupStageParam from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from result json file,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: swc_afc_algo.c
            Method_In_Test: AFC_SetupStageParam

            parent_suite: swc_fast_charge
            suite: afc_setup_stage_param
            sub_suite: setup_stage_param_coverage
            label: Integration
        """
    )
    def test_AFC_SetupStageParam_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input conditions to achieve improved
        code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        lib.AFC_Calc.Va_b_ValidSampleFlag = [1] * size(
            lib.AFC_Calc.Va_b_ValidSampleFlag
        )
        lib.AFC_Calc.Va_U_SampleSEVolt = [3200] * size(lib.AFC_Calc.Va_U_SampleSEVolt)
        lib.AFC_Calc.Va_Cnt_CPVCorrIdx = [5] * size(lib.AFC_Calc.Va_Cnt_CPVCorrIdx)

        set_lib_inputs(lib, test_cases)

        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )

        # Run Function
        # ------------------------------------------------
        lib.AFC_SetupStageParam()

        # Compare Results
        # ------------------------------------------------
        if not WRITE_STACK_PARAM_RESULTS:
            validate_test_cases(lib, test_cases, read_json_results)

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_SetupStageParam")
        logger.info(
            f"ACTUAL: AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
            f"AFC_Calc.Va_b_ValidSampleFlag={lib.AFC_Calc.Va_b_ValidSampleFlag},"
            f"AFC_Calc.Va_U_SampleSEVolt={lib.AFC_Calc.Va_U_SampleSEVolt},"
            f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt},"
            f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
        )
        # Log Stack-Parametrized Inputs
        # ------------------------------------------------
        if MAKE_HTML and LOG_STACK_PARAM_INPUTS:
            log_stack_parametrized_inputs(test_cases)

        # Optional: Log Stack-Parametrized Test Data
        # JSON file can be found in /buildoutputs/reports
        # ------------------------------------------------
        if WRITE_STACK_PARAM_RESULTS:
            vars_record = [
                "AFC_Calc.Ve_Cnt_PresentStgNum",
                "AFC_Calc.Va_b_ValidSampleFlag",
                "AFC_Calc.Va_U_SampleSEVolt",
                "VeAFC_U_ChgPackVolt",
                "VeAFC_I_ChgPackCurr",
            ]

            record_test_data(
                lib, test_cases, write_json_results, var_to_record=vars_record
            )
