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

ffi = cffi.FFI()

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

RUN_STACK_PARAM_TESTS = True  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = True  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)
MAKE_HTML = True
if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "tracking_flag": 0,
                    "AFC_Calc.Ve_e_QNS_State": 1,
                    "VeAPI_Pct_PackSOC": 9601,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3200] * 10,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [5] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 25,
                    "AFC_Calc.Ve_I_CV_Curr": 30000,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3200] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 30000,
                },
            },
            id="Test_Case_1_Start_New_Stage",
            marks=[
                mark.description(
                    "This test checks the various conditions when 'AFC_Calc.Ve_e_QNS_State' is in START_STAGE and "
                    "ensure that the value of 'AFC_Calc.Ve_e_QNS_State' changes from START_STAGE to "
                    "CeAFC_e_ContinueStage after execution."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "tracking_flag": 1,
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "VeAPI_Pct_PackSOC": 6371,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3900] * 10,
                    "AFC_Calc.Va_Cnt_CPVCorrIdx": [5] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_e_QNS_State": 1,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 13,
                    "AFC_Calc.Ve_I_CV_Curr": 30000,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3900] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 167000,
                },
            },
            id="Test_Case_2_CeAFC_e_ContinueStage",
            marks=[
                mark.description(
                    "This checks the main periodic under normal operating conditions in CONTINUE STAGE, specifically "
                    "during a stage transition due to SOC, executes CPV tracking and increment the stage."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "tracking_flag": 1,
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "VeAPI_Pct_PackSOC": 6371,
                    "VaAPI_U_SEVolts": [4500] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_e_QNS_State": 1,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 13,
                    "AFC_Calc.Ve_I_CV_Curr": 30000,
                    "AFC_Calc.Va_b_ValidSampleFlag": [0] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [0] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 191000,
                },
            },
            id="Test_Case_3_Over_Safety",
            marks=[
                mark.description(
                    "This checks for the scenario when cell voltages exceed the cell safety limit which triggers the "
                    "'Le_b_OverFlag' and forces increment to the next stage."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "tracking_flag": 1,
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "VeAPI_Pct_PackSOC": 6371,
                    "AFC_Param.Ka_U_Stg_SADCellLim": [0] * 25,
                    "VaAPI_U_SEVolts": [4200] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_e_QNS_State": 1,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 13,
                    "AFC_Calc.Ve_I_CV_Curr": 30000,
                    "AFC_Calc.Va_b_ValidSampleFlag": [0] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [0] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 191000,
                },
            },
            id="Test_Case_4_Over_CPV",
            marks=[
                mark.description(
                    "This checks for the scenario when cell voltages exceed the cell SAD limit which triggers the "
                    "'Le_b_OverCPVFlag' and forces increment to the next stage."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "tracking_flag": 1,
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "VeAPI_Pct_PackSOC": 6370 - 100,
                    "VaAPI_U_SEVolts": [3200] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 12,
                    "AFC_Calc.Ve_I_CV_Curr": 30000,
                    "AFC_Calc.Va_b_ValidSampleFlag": [1] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [3442] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 197000,
                },
            },
            id="Test_Case_5_GetSampleVoltage",
            marks=[
                mark.description(
                    "This checks for the condition when SOC is near the end of the stage (1%) to trigger the "
                    "conditions to get sample voltages for CPV tracking, therefore 'AFC_Calc.Va_b_ValidSampleFlag' == True."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
        param(
            {
                "Inputs": {
                    "tracking_flag": 1,
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 25,
                    "VeAPI_Pct_PackSOC": 9800,
                    "AFC_Calc.Ve_I_CV_Curr": 30000,  # assume controller initialized in constant voltage.
                    "VaAPI_U_SEVolts": [4250] * 10,
                },
                "Expected": {
                    "AFC_Calc.Ve_e_QNS_State": 2,
                    "AFC_Calc.Ve_Cnt_PresentStgNum": 25,
                    "AFC_Calc.Ve_I_CV_Curr": 29000,
                    "AFC_Calc.Va_b_ValidSampleFlag": [0] * 10,
                    "AFC_Calc.Va_U_SampleSEVolt": [0] * 10,
                    "VeAFC_U_ChgPackVolt": 816000,
                    "VeAFC_I_ChgPackCurr": 29000,
                },
            },
            id="Test_Case_6_ConstantVoltage",
            marks=[
                mark.description(
                    "This checks the scenario when in constant voltage condition, 'AFC_Calc.Ve_Cnt_PresentStgNum' should not "
                    "increment further, output current should be based off 'AFC_Calc.Ve_I_CV_Curr' and output voltage should "
                    "be based off of 'AFC_Param.Ke_U_CV_FloatSEVolt'."
                ),
                mark.jira_id("VCCFC-110"),
            ],
        ),
    ],
)
@allure.feature(
    """
        JIRA-ID: QAFC-90, QAFC-91, QAFC-92, QAFC-93, QAFC-94, QAFC-95, QAFC-96, QAFC-97, QAFC-98, QAFC-99, QAFC-100,\
        QAFC-102, QAFC-104, QAFC-105, QAFC-106, QAFC-107, QAFC-108, QAFC-109, QAFC-110, QAFC-111, QAFC-112

        Steps:\
        Step1: Have the source files ready for generating binary for swc_fast_charge.,\
        Step2: Generate binary (shared dll using cmake) using cmake,\
        3: StepInvoke method AFC_MainPrdc from afc binary via cffi using input param Le_T_CellTemp,\
        Step4: compare output with expected value from input param - sAFC_Calc.Ve_e_QNS_State, Ve_Cnt_PresentStgNum,
        Ve_I_CV_Curr, Va_b_ValidSampleFlag, Va_U_SampleCellVolt, VeAFC_U_ChgPackVolt, VeAFC_I_ChgPackCurr,\
        Step5: Test result should match with expected value,

        Source_File_In_Test: swc_afc_algo.c
        Method_In_Test: AFC_MainPrdc

        parent_suite: swc_fast_charge
        suite: afc_main_prdc
        sub_suite: main_prdc
    """
)
def test_AFC_MainPrdc(lib, setup_parameters, test_cases) -> None:
    """
    This test function performs verification of specific operating conditions relevant to the 'AFC_MainPrdc' function.
    """

    # Setup Variables
    # ------------------------------------------------
    tracking_flag = test_cases["Inputs"]["tracking_flag"]
    set_lib_inputs(lib, test_cases)

    lib.AFC_SetInputs(
        ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
    )

    # Run Function
    # ------------------------------------------------
    lib.AFC_MainPrdc(tracking_flag)

    # Use these lines for updating testrail when required
    # log_for_testrail_update("AFC_MainPrdc")
    logger.info(
        f"ACTUAL: AFC_Calc.Ve_e_QNS_State={lib.AFC_Calc.Ve_e_QNS_State},"
        f"AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
        f"AFC_Calc.Ve_I_CV_Curr={lib.AFC_Calc.Ve_I_CV_Curr},"
        f"AFC_Calc.Va_b_ValidSampleFlag={lib.AFC_Calc.Va_b_ValidSampleFlag},"
        f"AFC_Calc.Va_U_SampleSEVolt={lib.AFC_Calc.Va_U_SampleSEVolt},"
        f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt},"
        f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
    )

    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)


# =======================================================================
# Stack-Parametrized Test Cases for Code Coverage
# =======================================================================
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "VeAPI_Pct_PackSOC": [50, 7900, 10000],
        "AFC_Calc.Ve_Cnt_PresentStgNum": [0, 20, 22, 25],
        "AFC_Calc.Ve_e_QNS_State": [0, 1, 2],
        "VaAPI_U_SEVolts": [([x] * 10) for x in [0, 3500, 4200, 4500]],
        "VeAPI_T_MinTempSnsr": [0, 360],
        "VeAPI_T_MaxTempSnsr": [550, 990],
        "INP_Snsr.Ke_n_NumCellSeries": [1, 10],
        "Le_b_CPVTrackingFlag": [0, 1],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)
    @allure.feature(
        """
            JIRA-ID: QAFC-90, QAFC-91, QAFC-92, QAFC-93, QAFC-94, QAFC-95, QAFC-96, QAFC-97, QAFC-98, QAFC-99, QAFC-100,\
            QAFC-102, QAFC-104, QAFC-105, QAFC-106, QAFC-107, QAFC-108, QAFC-109, QAFC-110, QAFC-111, QAFC-112

            Steps:\
            Step1: StepHave the source files ready for generating binary for swc_fast_charge.,\
            Step2: Generate binary (shared dll using cmake) using cmake,\
            Step3: Invoke method AFC_MainPrdc from afc binary via cffi using input param Le_T_CellTemp,\
            Step4: compare output with expected value from result json file,\
            Step5: Test result should match with expected value,

            Source_File_In_Test: swc_afc_algo.c
            Method_In_Test: AFC_MainPrdc

            parent_suite: swc_fast_charge
            suite: afc_main_prdc
            sub_suite: main_prdc_coverage
            label: Integration
        """
    )
    def test_AFC_MainPrdc_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input conditions to achieve improved
        code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        tracking_flag = test_cases["Inputs"]["Le_b_CPVTrackingFlag"]
        set_lib_inputs(lib, test_cases)

        lib.AFC_SetInputs(
            ffi.addressof(lib, "AFC_Inputs"), ffi.addressof(lib, "AFC_Outputs")
        )

        # Run Function
        # ------------------------------------------------
        lib.AFC_MainPrdc(tracking_flag)

        # Compare Results
        # ------------------------------------------------
        if not WRITE_STACK_PARAM_RESULTS:
            if lib.AFC_Calc.Ve_I_CV_Curr >= 1590138752:
                pytest.xfail(
                    "Known issue where signed to unsigned changes 'AFC_Calc.Ve_I_CV_Curr' results from -1000A."
                )
            else:
                validate_test_cases(lib, test_cases, read_json_results)

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_MainPrdc")
        logger.info(
            f"ACTUAL: AFC_Calc.Ve_e_QNS_State={lib.AFC_Calc.Ve_e_QNS_State},"
            f"AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
            f"AFC_Calc.Ve_I_CV_Curr={lib.AFC_Calc.Ve_I_CV_Curr},"
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
                "AFC_Calc.Ve_e_QNS_State",
                "AFC_Calc.Ve_Cnt_PresentStgNum",
                "AFC_Calc.Ve_I_CV_Curr",
                "AFC_Calc.Va_b_ValidSampleFlag",
                "AFC_Calc.Va_U_SampleSEVolt",
                "VeAFC_U_ChgPackVolt",
                "VeAFC_I_ChgPackCurr",
            ]

            record_test_data(
                lib, test_cases, write_json_results, var_to_record=vars_record
            )
