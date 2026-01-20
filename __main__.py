"""This main test module serves as an indicator for TAF to trigger pytest, executing all test cases in this tst
directory. Additionally, it sets up necessary imports and parameters for other test modules in this 'tst' directory to
leverage."""

import ast
import csv
from os.path import abspath, dirname, join
from pathlib import Path

import cffi
import numpy as np
import pytest
import random
from pytest import fixture, mark, param
from src.common import (
    PROJECT_PATH,
    clean_dat_files,
    compare_result,
    get_lib_callables,
    invoke_pytest,
    lib,
    lib_array_to_list,
    log_stack_parametrized_inputs,
    parametrize_args,
    read_json_results,
    record_test_data,
    set_lib_inputs,
    size,
    validate_test_cases,
    write_json_results,
    iter_file,
    write_output_to_excel,
)

MAKE_HTML = True  # Set true to allow html report generation.

ffi = cffi.FFI()


@fixture(scope="function")
def setup_parameters(lib) -> None:
    """This fixture initializes the global variables in the specified library module at the beginning of each test
    function. These variables are reset to their initial values for every standard and parametrized test case, ensuring
    consistent test conditions.

    Args:
        lib (module): The shared library module, either a .dll (Windows) or .so (Unix/Linux) file, containing the global
         variables to be initialized.
    """

    # Data Ready Signals
    # ------------------------------------------------
    lib.VeAPI_b_PackCurr_DR = 1
    lib.VaAPI_b_CellVolts_DR = [1] * size(lib.VaAPI_b_CellVolts_DR)
    lib.VaAPI_b_TempSnsrs_DR = [1] * size(lib.VaAPI_b_TempSnsrs_DR)
    lib.VeAPI_b_MinTempSnsr_DR = 1
    lib.VeAPI_b_MaxTempSnsr_DR = 1
    lib.VeAPI_b_ChgPackCapcty_DR = 1
    lib.VeAPI_b_PackSOC_DR = 1

    # NVM Initialization
    # ------------------------------------------------
    lib.VeAFC_b_ControllerWakeUp = 0
    lib.VeAFC_b_Initialized = 0
    lib.VeAPI_b_EVSEChgStatus = 1
    lib.VeAPI_I_PackCurr = 1



    lib.fs_API_SetInputsAFC(
        lib.VaAPI_Cmp_NVMRegion,
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
    )

    lib.f_AFC_NVMInit()
    lib.qnovo_cte_init()

    #lib.f_AFC_NVMInit()


    # Calculation
    # ------------------------------------------------
    lib.s_AFC_Calc.VeAFC_e_QNS_State = 0
    lib.s_AFC_Calc.VeAFC_Cnt_PresentStgNum = 0
    lib.s_AFC_Calc.VeAFC_I_CV_Curr = lib.s_AFC_Param.KeAFC_I_CV_ChgCurr
    lib.s_AFC_Calc.VaAFC_b_ValidSampleFlag = [0] * size(
        lib.s_AFC_Calc.VaAFC_b_ValidSampleFlag
    )
    lib.s_AFC_Calc.VaAFC_U_SampleCellVolt = [0] * size(
        lib.s_AFC_Calc.VaAFC_U_SampleCellVolt
    )

    lib.VeAPI_T_MinTempSnsr = 350
    lib.VeAPI_T_MaxTempSnsr = 565

    lib.s_AFC_Calc.VeAFC_T_StdU_RefCellTemp = 350.0 / 10.0

    # Customer Inputs
    # ------------------------------------------------
    lib.KeINP_n_MaxNumCells = 192
    lib.KeINP_n_MaxNumTempSnsrs = 18
    lib.KaINP_i_Temp2CellIdx = [i // 12 for i in range(192)]

    lib.VeAPI_Pct_PackSOC = 5000
    lib.VeAPI_Cap_ChgPackCapcty = 120600

    random.seed(44)
    noise_mV = [random.uniform(-100, 100) for _ in range(size(lib.VaAPI_U_CellVolts))]
    lib.VaAPI_U_CellVolts = [3200 + int(noise_mV[i]) for i in range(size(lib.VaAPI_U_CellVolts))]

    # lib.VaAPI_U_CellVolts = [3200] * size(lib.VaAPI_U_CellVolts)

    lib.VaAPI_T_TempSnsrs = [-150 + i * 50 for i in range(size(lib.VaAPI_T_TempSnsrs) - 2)]
    lib.VaAPI_T_TempSnsrs[size(lib.VaAPI_T_TempSnsrs) - 2] = min(list(lib.VaAPI_T_TempSnsrs))
    lib.VaAPI_T_TempSnsrs[size(lib.VaAPI_T_TempSnsrs) - 1] = max(list(lib.VaAPI_T_TempSnsrs))

    # lib.VaAPI_T_TempSnsrs = [-100 + i * 50 for i in range(size(lib.VaAPI_T_TempSnsrs))]

    # lib.VaAPI_T_TempSnsrs = [350] * size(lib.VaAPI_T_TempSnsrs)

    lib.VeAPI_I_PackCurr = 500

    # Customer Outputs
    # ------------------------------------------------
    lib.VeAFC_e_ErrorFlags = 0
    lib.VeAFC_I_ChgPackCurr = 0
    lib.VeAFC_U_ChgPackVolt = 0
    lib.VeAFC_b_ChgCompletionFlag = 0

    # OCV vs. SOC
    # ------------------------------------------------
    lib.KaLIB_U_OCVAxis = [
        2583,
        2636,
        2682,
        2721,
        2756,
        2786,
        2814,
        2840,
        2885,
        2905,
        2940,
        2969,
        2995,
        3019,
        3040,
        3060,
        3087,
        3111,
        3139,
        3164,
        3187,
        3228,
        3271,
        3306,
        3335,
        3355,
        3370,
        3379,
        3396,
        3437,
        3497,
        3534,
        3565,
        3597,
        3665,
        3685,
        3704,
        3727,
        3754,
        3772,
        3815,
        3845,
        3870,
        3891,
        3933,
        3952,
        3976,
        4028,
        4048,
        4060,
        4068,
        4074,
        4088,
        4097,
        4106,
        4121,
        4140,
        4151,
        4165,
        4180,
        4195,
    ]

    lib.KaLIB_Pct_SOCAxis = [
        0,
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        90,
        100,
        120,
        140,
        160,
        180,
        200,
        220,
        250,
        280,
        320,
        360,
        400,
        480,
        580,
        670,
        760,
        840,
        910,
        960,
        1090,
        1520,
        2000,
        2350,
        2710,
        3120,
        4210,
        4490,
        4730,
        4970,
        5230,
        5380,
        5690,
        5970,
        6240,
        6500,
        7130,
        7370,
        7610,
        8080,
        8290,
        8440,
        8590,
        8750,
        9270,
        9440,
        9570,
        9700,
        9810,
        9860,
        9910,
        9960,
        10000
    ]

    # NVM
    # ------------------------------------------------
    size_row, size_col = size(lib.s_AFC_Track.NtAFC_Cnt_CPVCorrIdx)
    lib.s_AFC_Track.NtAFC_Cnt_CPVCorrIdx = [[0] * size_col for _ in range(size_row)]

    size_row, size_col = size(lib.s_AFC_Track.NtAFC_U_RefCellVolt)
    lib.s_AFC_Track.NtAFC_U_RefCellVolt = [[0] * size_col for _ in range(size_row)]

    lib.s_AFC_Calc.VaAFC_Cnt_CPVCorrIdx = [0] * size(
        lib.s_AFC_Calc.VaAFC_Cnt_CPVCorrIdx
    )
    lib.s_AFC_Calc.VaAFC_U_RefCellVolt = [0] * size(lib.s_AFC_Calc.VaAFC_U_RefCellVolt)

    # Parameters/Calibrations, based on Volvo battery cell characterization
    # ------------------------------------------------
    lib.sAFC_P.Ve_U_CVFloatCellVolt = 4200
    lib.sAFC_P.Ve_U_SafetyMaxVolt = 4200

    lib.s_AFC_Param.KeAFC_U_CV_RatedChgCellVolt = 4200
    lib.s_AFC_Param.KeAFC_I_CV_ChgCurr = 24200
    lib.s_AFC_Param.KeAFC_I_CV_ChgStepCurr = 500

    lib.s_AFC_Param.KaAFC_Pct_Stg_SOC = [
        1390,
        2110,
        2660,
        3220,
        3770,
        4330,
        4880,
        5400,
        5890,
        6360,
        6780,
        7160,
        7490,
        7770,
        7860,
        8580,
        9010,
        9310,
        9530,
        9700
    ]

    lib.s_AFC_Param.KaAFC_I_Stg_ChgMaxCurr = [  # mA
        331600,
        331600,
        331600,
        331600,
        331600,
        331600,
        329200,
        313400,
        296600,
        277000,
        253600,
        226400,
        197000,
        167200,
        138600,
        94200,
        62000,
        46000,
        36200,
        30200
    ]

    lib.s_AFC_Param.KaAFC_I_Stg_ChgMinCurr = [  # mA
        170600,
        170600,
        170600,
        170600,
        170600,
        170600,
        168200,
        152400,
        135600,
        116000,
        113600,
        107400,
        98400,
        68600,
        59400,
        54200,
        44000,
        30000,
        28200,
        24200
    ]

    lib.s_AFC_Param.KaAFC_I_Stg_ChgStepCurr = [  # mA
        4600,
        4600,
        4600,
        4600,
        4600,
        4600,
        4600,
        4600,
        4600,
        4600,
        4000,
        3400,
        2900,
        2900,
        2400,
        2000,
        2000,
        2000,
        1000,
        1000
    ]

    lib.s_AFC_Param.KaAFC_U_Stg_RefStartCellVolt = [  # mV
        3951,
        3952,
        3962,
        3974,
        3995,
        4022,
        4055,
        4074,
        4095,
        4115,
        4130,
        4139,
        4144,
        4147,
        4149,
        4190,
        4190,
        4190,
        4190,
        4190
    ]

    lib.s_AFC_Param.KaAFC_U_Stg_RefBandCellVolt = [4] * size(
        lib.s_AFC_Param.KaAFC_U_Stg_RefBandCellVolt
    )

    lib.s_AFC_Param.KaAFC_U_Stg_SADCellLim = [
        4051,
        4052,
        4062,
        4074,
        4095,
        4112,
        4135,
        4144,
        4155,
        4165,
        4170,
        4179,
        4184,
        4187,
        4189,
        4190,
        4190,
        4190,
        4190,
        4190
    ]

    lib.s_AFC_Param.KeAFC_T_CPV_MaxTempLim = 565
    lib.s_AFC_Param.KeAFC_T_CPV_MinTempLim = -100
    lib.s_AFC_Param.KeAFC_T_RefTemp = 350
    lib.s_AFC_Param.KeAFC_k_Coeff_a = 0.00045776
    lib.s_AFC_Param.KeAFC_k_Coeff_b = -0.01351100
    lib.s_AFC_Param.KeAFC_k_Coeff_c = 0.0000044631
    lib.s_AFC_Param.KeAFC_k_Coeff_d = 0.41610019
    lib.s_AFC_Param.KeAFC_k_Coeff_e = 0.01043331
    lib.s_AFC_Param.KeAFC_k_Coeff_f = 0.70483405
    lib.s_AFC_Param.KeAFC_k_Coeff_g = -0.01518426
    lib.s_AFC_Param.KeAFC_k_Coeff_h = 1.38684589

    # Unused variables (commented for possibility of future implementations)
    # ------------------------------------------------
    # lib.g_num_temps = 4
    # lib.adc_VOLT_STACK = sum(lib.VaAPI_U_CellVolts)
    # lib.VeAPI_T_MaxTempSnsr = 4200
    # lib.adc_VOLT_MIN = 3000

    yield

    clean_dat_files(PROJECT_PATH)


if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    invoke_pytest(current_dir, html=MAKE_HTML)
