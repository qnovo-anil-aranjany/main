"""Test Module Description:
    Test module for AFC Voltage Imbalance.

Requirements:
    - [JIRA ticket or requirement reference]
    - Python version >= 3.10.4
    - Pytest version >= 7.4.3
"""


from .__main__ import *

ffi = cffi.FFI()

# Optional Flags:
# ------------------------------------------------
SKIP_MODULE = False  # Set to True to skip all test cases in this module.

RUN_STACK_PARAM_TESTS = True  # Set True to run stack-parametrized testing.
LOG_STACK_PARAM_INPUTS = False  # Set True to log stack-parametrized inputs into html.
WRITE_STACK_PARAM_RESULTS = (
    False  # Set True to write stack-parametrized results into JSON.
)
MAKE_HTML = True
if SKIP_MODULE:
    pytestmark = pytest.mark.skip(reason="All test cases in this module are skipped.")


_NUM_SE = 192


@pytest.mark.parametrize(
    "test_cases",
    [
        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 4,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 8,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 1,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3203,
                        3204,
                        3205,
                        3206,
                        3207,
                        3208,
						3209,
                        3210,
						3211,
						3212,
						3213,
						3214,
						3215,
						3216,
						3217,
						3218,
						3219,
						3220,
                        3221,
                        3222,
                        3223,
                        3224,
                        3225,
                        3226,
                        3227,
						3228,
                        3229,
						3230,
						3231,
						3232,
						3233,
						3234,
						3235,
						3236,
						3237,
						3238,
						3239,
                        3240,
                        3241,
                        3242,
                        3243,
                        3244,
                        3245,
                        3246,
						3247,
                        3248,
						3249,
						3250,
						3251,
						3252,
						3253,
						3254,
						3255,
						3256,
						3257,
						3258,
                        3259,
                        3260,
                        3261,
                        3262,
                        3263,
                        3264,
                        3265,
						3266,
                        3267,
						3268,
						3269,
						3270,
						3271,
						3272,
						3273,
						3274,
						3275,
						3276,
						3277,
                        3278,
                        3279,
                        3280,
                        3281,
                        3282,
                        3283,
                        3284,
						3285,
                        3286,
						3287,
						3288,
						3289,
						3290,
						3291,
						3292,
						3293,
						3294,
						3295,
						3296,
                        3297,
                        3298,
                        3299,
                        3300,
                        3301,
                        3302,
                        3303,
						3304,
                        3305,
						3306,
						3307,
						3308,
						3309,
						3310,
						3311,
						3312,
						3313,
						3314,
						3315,
                        3316,
                        3317,
                        3318,
                        3319,
                        3340,
                        3341,
                        3342,
						3343,
                        3344,
						3345,
						3346,
						3347,
						3348,
						3349,
						3350,
						3351,
						3352,
						3353,
						3354,
                        3355,
                        3356,
                        3357,
                        3358,
                        3359,
                        3360,
                        3361,
						3362,
                        3363,
						3364,
						3365,
						3366,
						3367,
						3368,
						3369,
						3370,
						3371,
						3372,
						3373,
                        3374,
                        3375,
                        3376,
						3377,
                        3378,
						3379,
						3380,
						3381,
						3382,
						3383,
						3384,
						3385,
						3386,
						3387,
						3388,
                        3389,
                        3390,
                        3391,
						3392,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 1,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0 for i in range(192)],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_ErrorFlags": 0,
                },
            },
            id="Test_Case_0",
            marks=[
                mark.description(
                    "Normal working condition, detected one SE with voltage imbalances."
                ),
            ],
        ),

        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 4,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 8,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 1,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3179,
                        3203,
                        3204,
                        3205,
                        3206,
                        3207,
                        3208,
                        3209,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [0]
                                                                              * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [0]
                                                                                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 1,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_WarningFlags": 0,
                },
            },
            id="Test_Case_1",
            marks=[
                mark.description(
                    "Normal working condition, detected one SE with voltage imbalances."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 4,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 8,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 1,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3179,
                        3203,
                        3179,
                        3205,
                        3206,
                        3207,
                        3208,
                        3209,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 1,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [
                        0,
                        0,
                        1,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_ErrorFlags": 0,
                },
            },
            id="Test_Case_2",
            marks=[
                mark.description(
                    "Normal working condition, detected two SE with voltage imbalances."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 4,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 8,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3179,
                        3203,
                        3179,
                        3205,
                        3206,
                        3207,
                        3208,
                        3209,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 1,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3179,
                        3203,
                        3179,
                        3205,
                        3206,
                        3207,
                        3208,
                        3209,
                    ],
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_ErrorFlags": 0,
                },
            },
            id="Test_Case_3",
            marks=[
                mark.description("Analysis flag was not ready."),
            ],
        ),
        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 4,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 8,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 1,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3179,
                        3203,
                        3179,
                        3205,
                        3206,
                        3207,
                        3208,
                        3209,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [3200]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [
                        3500
                    ]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 1,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [1] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [
                        0,
                        0,
                        1,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_ErrorFlags": 0,
                },
            },
            id="Test_Case_4",
            marks=[
                mark.description(
                    "Check robustness of function if volatile carried over from previous run or if it contained unintended values."
                ),
            ],
        ),
        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 4,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 8,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 1,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 1,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_ErrorFlags": 16384,
                },
            },
            id="Test_Case_5",
            marks=[
                mark.description("Set VoltageSumMAD to 0 and trigger warning."),
            ],
        ),
        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 4,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 8,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 1,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3179,
                        3203,
                        3204,
                        3205,
                        3206,
                        3207,
                        3208,
                        3209,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_ErrorFlags": 16384,
                },
            },
            id="Test_Case_6",
            marks=[
                mark.description("Set Ve_t_SamplingTime to 0 and trigger warning."),
            ],
        ),
        param(
            {
                "Inputs": {
                    "lib.KeINP_n_MaxNumCells": _NUM_SE,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": 0,
                    "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": 0,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 1,
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
                        3201,
                        3202,
                        3179,
                        3203,
                        3204,
                        3205,
                        3206,
                        3207,
                        3208,
                        3209,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [0]
                    * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 1,
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [0] * _NUM_SE,
                },
                "Expected": {
                    "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [
                        1,
                        1,
                        1,
                        1,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [0] * _NUM_SE,
                    "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": 0,
                    "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": 0,
                    "VeAFC_e_ErrorFlags": 16384,
                },
            },
            id="Test_Case_7",
            marks=[
                mark.description(
                    "Set Le_U_VoltageImbalanceThreshold to 0 and trigger warning."
                ),
            ],
        ),
    ],
)

def test_AFC_VoltageImbalance_Analysis(lib, setup_parameters, test_cases) -> None:
    """
    Verify the functionality of voltage imbalance analysis within source code implementation.
    """
    # Setup Variables
    # ------------------------------------------------
    set_lib_inputs(lib, test_cases)

    lib.fs_API_SetInputsAFC(
        lib.VaAPI_Cmp_NVMRegion,
        lib.VaAPI_Cmp_NVMLoggingRegion,
        lib.VeAPI_I_PackCurr,
        lib.VeAPI_b_PackCurr_DR,
        lib.VaAPI_U_CellVolts,
        lib.VaAPI_b_CellVolts_DR,
        lib.VaAPI_T_TempSnsrs,
        lib.VaAPI_b_TempSnsrs_DR,
        lib.VeAPI_T_MinTempSnsr,
        lib.VeAPI_b_MinTempSnsr_DR,
        lib.VeAPI_T_MaxTempSnsr,
        lib.VeAPI_b_MaxTempSnsr_DR,
        lib.VeAPI_Cap_ChgPackCapcty,
        lib.VeAPI_b_ChgPackCapcty_DR,
        lib.VeAPI_Pct_PackSOC,
        lib.VeAPI_b_PackSOC_DR,
        lib.VeAPI_b_EVSEChgStatus,
        ffi.addressof(lib, "VaAFC_Cmp_CTE_Info"),
        ffi.addressof(lib, "VeAFC_e_ErrorFlags"),
        ffi.addressof(lib, "VeAFC_I_ChgPackCurr"),
        ffi.addressof(lib, "VeAFC_U_ChgPackVolt"),
        ffi.addressof(lib, "VeAFC_b_ChgCompletionFlag"),
        ffi.addressof(lib, "VeAFC_b_ExtremeAgingFlag"),
        ffi.addressof(lib, "VeAFC_b_AbnormalAgingFlag"),
        ffi.addressof(lib, "VeAFC_b_EarlyWarningAgingFlag"),
        ffi.addressof(lib, "VeAFC_b_EOLFlag"),
        ffi.addressof(lib, "VeAFC_b_SOCImbalanceFlag"),
    )

    # Run Function
    # ------------------------------------------------
    lib.AFC_VoltageImbalance_Analysis()

    # Use these lines for updating testrail when required
    # logger.info(
    #     f"ACTUAL: AFC_Calc.Ve_e_QNS_State={lib.AFC_Calc.Ve_e_QNS_State},"
    #     f"AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
    #     f"AFC_Calc.Ve_I_CV_Curr={lib.AFC_Calc.Ve_I_CV_Curr},"
    #     f"AFC_Calc.Va_b_ValidSampleFlag={lib.AFC_Calc.Va_b_ValidSampleFlag},"
    #     f"AFC_Calc.Va_U_SampleSEVolt={lib.AFC_Calc.Va_U_SampleSEVolt},"
    #     f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt},"
    #     f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
    # )

    # Compare Results
    # ------------------------------------------------
    validate_test_cases(lib, test_cases)


# =======================================================================
# Stack-Parametrized Test Cases for Code Coverage
# =======================================================================
_NUM_SE = 192
if RUN_STACK_PARAM_TESTS:
    param_inputs = {
        "INP_Snsr.Ke_n_NumCellSeries": [_NUM_SE],
        "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel": [0, 2, 4, 8],
        "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor": [0, 2, 4, 8],
        "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis": [0, 1],
        "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums": [
            [3201, 3202, 3179, 3203, 3204, 3205, 3206, 3207, 3208, 3209]
            + [3205] * (_NUM_SE - 10)
        ],
        "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort": [[0] * _NUM_SE],
        "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations": [[0] * _NUM_SE],
        "AFC_VM_VoltageImbalance.Ve_t_SamplingTime": [0, 1, 2],
        "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags": [[0] * _NUM_SE],
        "QnovoAFC_Log_VoltageImbalance_ZScore": [[0.0] * _NUM_SE],
        "QnovoAFC_Log_VoltageImbalance_Threshold": [0],
    }

    combinations, ids = parametrize_args(param_inputs)

    @pytest.mark.parametrize("test_cases", combinations, ids=ids)

    def Atest_AFC_VoltageImbalance_Analysis_coverage(
        lib, setup_parameters, test_cases, read_json_results, write_json_results
    ) -> None:
        """
        This test function executes stack parametrization tests across a range of input
        conditions to achieve improved code coverage.
        """

        # Setup Variables
        # ------------------------------------------------
        set_lib_inputs(lib, test_cases)

        # Run Function
        # ------------------------------------------------
        lib.AFC_VoltageImbalance_Analysis()

        # Compare Results
        # ------------------------------------------------
        if not WRITE_STACK_PARAM_RESULTS:
            validate_test_cases(lib, test_cases, read_json_results)

        # Use these lines for updating testrail when required
        # log_for_testrail_update("AFC_MainPrdc")
        # logger.info(
        #     f"ACTUAL: AFC_Calc.Ve_e_QNS_State={lib.AFC_Calc.Ve_e_QNS_State},"
        #     f"AFC_Calc.Ve_Cnt_PresentStgNum={lib.AFC_Calc.Ve_Cnt_PresentStgNum},"
        #     f"AFC_Calc.Ve_I_CV_Curr={lib.AFC_Calc.Ve_I_CV_Curr},"
        #     f"AFC_Calc.Va_b_ValidSampleFlag={lib.AFC_Calc.Va_b_ValidSampleFlag},"
        #     f"AFC_Calc.Va_U_SampleSEVolt={lib.AFC_Calc.Va_U_SampleSEVolt},"
        #     f"VeAFC_U_ChgPackVolt={lib.VeAFC_U_ChgPackVolt},"
        #     f"VeAFC_I_ChgPackCurr={lib.VeAFC_I_ChgPackCurr}"
        # )

        # Log Stack-Parametrized Inputs
        # ------------------------------------------------
        if MAKE_HTML and LOG_STACK_PARAM_INPUTS:
            log_stack_parametrized_inputs(test_cases)

        # Optional: Log Stack-Parametrized Test Data
        # JSON file can be found in /buildoutputs/reports
        # ------------------------------------------------
        if WRITE_STACK_PARAM_RESULTS:
            vars_record = [
                "INP_Snsr.Ke_n_NumCellSeries",
                "AFC_Param_VoltageImbalance.Ke_Cmp_SigmaLevel",
                "AFC_Param_VoltageImbalance.Ke_Cmp_NoiseFloor",
                "AFC_VM_VoltageImbalance.Ve_b_ReadyForAnalysis",
                "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums",
                "AFC_VM_VoltageImbalance.Va_U_SE_ChargeVoltageSums_Sort",
                "AFC_VM_VoltageImbalance.Va_U_SE_AbsoluteVoltageSumDeviations",
                "AFC_VM_VoltageImbalance.Ve_t_SamplingTime",
                "AFC_VM_VoltageImbalance.Va_b_VoltageImbalanceFlags",
                "QnovoAFC_Log_VoltageImbalance_ZScore",
                "QnovoAFC_Log_VoltageImbalance_Threshold",
                "VeAFC_e_WarningFlags",
            ]

            record_test_data(
                lib,
                test_cases,
                write_json_results,
                var_to_record=vars_record,
            )
