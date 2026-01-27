/**********************************************************************
 * This file is to allow source code to compile for testing purposes.
 **********************************************************************/

#ifdef UNITTEST

/************************************************
 * Include Header Files
 ************************************************/
#include "test_config.h"
#include "qnovo_afc_api.h"


/************************************************
 * Global Variables: Mock I/O
 ************************************************/
/* Inputs from Customers */
t_uint32            VaAPI_Cmp_NVMRegion[NVM_ARRAY_SIZE];
t_uint32            VeAPI_n_NVMRegionSize = sizeof(VaAPI_Cmp_NVMRegion);
t_uint8            VaAPI_Cmp_NVMLoggingRegion[NVM_LOG_SIZE];
t_uint32            VeAPI_n_NVMLoggingRegion = sizeof(VaAPI_Cmp_NVMLoggingRegion);
t_Pct_percent       VeAPI_Pct_PackSOC;
t_bool              VeAPI_b_PackSOC_DR;
t_I_milliamp        VeAPI_I_PackCurr;
t_bool              VeAPI_b_PackCurr_DR;
t_U_millivolt_cell  VaAPI_U_SEVolts[NUM_CELL_SERIES];
t_bool              VaAPI_b_SEVolts_DR[NUM_CELL_SERIES];
t_T_celsius         VaAPI_T_TempSnsrs[NUM_TEMP_SNSRS];
t_bool              VaAPI_b_TempSnsrs_DR[NUM_TEMP_SNSRS];
t_T_celsius         VeAPI_T_MinTempSnsr;
t_bool              VeAPI_b_MinTempSnsr_DR;
t_T_celsius         VeAPI_T_MaxTempSnsr;
t_bool              VeAPI_b_MaxTempSnsr_DR;
t_Cap_milliamphr    VeAPI_Cap_ChgPackCapcty;
t_bool              VeAPI_b_ChgPackCapcty_DR;
t_bool              VeAPI_b_EVSEChgStatus;
t_int32             VeAPI_e_EVSEChgLevel;
t_float32           VeAPI_e_Ab;
t_float32           VeAPI_e_Dp;
t_T_celsius         VeAPI_e_Tbgn;
t_T_celsius         VeAPI_e_Tlim;
t_float32           VeAPI_e_Alpha;
t_bool              VeAPI_e_NVMReset;
t_T_celsius         VeAPI_e_ChillerOnTemp;
t_uint32            VeAPI_e_TuningState;
t_bool              VeAFC_b_ExtremeAgingFlag;
t_bool              VeAFC_b_AbnormalAgingFlag;
t_bool              VeAFC_b_EarlyWarningAgingFlag;
t_bool              VeAFC_b_EOLFlag;
t_bool              VeAFC_b_SOCImbalanceFlag;

struct AFC_Inputs_t AFC_Inputs = {
    .NVMRegion 		= VaAPI_Cmp_NVMRegion,
    .NVMRegionSize     = &VeAPI_n_NVMRegionSize,
    .NVMLoggingRegion 		= VaAPI_Cmp_NVMLoggingRegion,
    .NVMLoggingRegionSize     = &VeAPI_n_NVMLoggingRegion,
    .PackSOC			= &VeAPI_Pct_PackSOC,
    .PackSOC_DR 		= &VeAPI_b_PackSOC_DR,
    .PackCurr 			= &VeAPI_I_PackCurr,
    .PackCurr_DR 		= &VeAPI_b_PackCurr_DR,
    .SEVolts 			= VaAPI_U_SEVolts,
    .SEVolts_DR 		= VaAPI_b_SEVolts_DR,
    .TempSnsrs 			= VaAPI_T_TempSnsrs,
    .TempSnsrs_DR 		= VaAPI_b_TempSnsrs_DR,
    .MinTempSnsr 		= &VeAPI_T_MinTempSnsr,
    .MinTempSnsr_DR		= &VeAPI_b_MinTempSnsr_DR,
    .MaxTempSnsr 		= &VeAPI_T_MaxTempSnsr,
    .MaxTempSnsr_DR 	= &VeAPI_b_MaxTempSnsr_DR,
    .ChgPackCapcty 		= &VeAPI_Cap_ChgPackCapcty,
    .ChgPackCapcty_DR	= &VeAPI_b_ChgPackCapcty_DR,
    .EVSEChgStatus 		= &VeAPI_b_EVSEChgStatus,
    .EVSEChgLevel       = &VeAPI_e_EVSEChgLevel,
    .TuningState        = &VeAPI_e_TuningState,
    .Ab                 = &VeAPI_e_Ab,
    .Dp                 = &VeAPI_e_Dp,
    .Tbgn               = &VeAPI_e_Tbgn,
    .Tlim               = &VeAPI_e_Tlim,
    .Alpha              = &VeAPI_e_Alpha,
    .NVMReset           = &VeAPI_e_NVMReset,
    .ChillerOnTemp      = &VeAPI_e_ChillerOnTemp,
};

/* Outputs to Customers */
t_uint8				VaAFC_Cmp_AFC_to_CTE_Info[AFC_to_CTE_INFO_ARRAY_SIZE];
t_uint32            VeAFC_e_WarningFlags;
t_I_milliamp_chg    VeAFC_I_ChgPackCurr;
t_U_millivolt_pack  VeAFC_U_ChgPackVolt;
t_bool              VeAFC_b_ChgCompletionFlag;

struct AFC_Outputs_t AFC_Outputs = {
	.AFC_to_CTE_Info	= &VaAFC_Cmp_AFC_to_CTE_Info,
    .WarningFlags 		= &VeAFC_e_WarningFlags,
    .ChgPackCurr 		= &VeAFC_I_ChgPackCurr,
    .ChgPackVolt 		= &VeAFC_U_ChgPackVolt,
    .ChgCompletionFlag 	= &VeAFC_b_ChgCompletionFlag,
    .ExtremeAgingFlag    = &VeAFC_b_ExtremeAgingFlag,
    .AbnormalAgingFlag  = &VeAFC_b_AbnormalAgingFlag,
    .EarlyWarningAgingFlag = &VeAFC_b_EarlyWarningAgingFlag,
    .EOLFlag               = &VeAFC_b_EOLFlag,
    .SOCImbalanceFlag      = &VeAFC_b_SOCImbalanceFlag,
};

/* Obfuscation */
t_int32 VeAPI_Cmp_LogSrc;
t_uint32 VeAPI_Cmp_LogSrcSize = sizeof(VeAPI_Cmp_LogSrc);
t_int32 VeAPI_Cmp_LogDst;

t_int32 VeAPI_Cmp_LogSrcArray[GENERIC_LOG_ARRAY_SIZE];
t_uint32 VeAPI_Cmp_LogSrcArraySize = sizeof(VeAPI_Cmp_LogSrcArray);
t_int32 VeAPI_Cmp_LogDstArray[GENERIC_LOG_ARRAY_SIZE];
t_U_millivolt_cell  cell_volts_temp[192];
LIB_CircBuffHandle_t Input_CircBuffHandle_t;
t_uint8*             ele_addr;



#else
#endif

/************************************************
 * Function Definitions
 ************************************************/
int main(void) {
  return 0;
}
