/**********************************************************************
 * This file is to allow source code to compile for testing purposes.
 **********************************************************************/

#ifndef TEST_CONFIG_H_
#define TEST_CONFIG_H_

#ifdef UNITTEST

/************************************************
 * Include Header Files
 ************************************************/
#include <stdio.h>

#include "cfg_global_defs.h"
#include "qnovo_bms_config.h"
#include "lib_common_utils.h"
#include "qnovo_afc_api.h"



/************************************************
 * Macro Definitions
 ************************************************/
#define NVM_ARRAY_SIZE              13000
#define NVM_LOG_SIZE 4000
#define AFC_to_CTE_INFO_ARRAY_SIZE  44
#define GENERIC_LOG_ARRAY_SIZE      100


/************************************************
 * Global Variables: Mock I/O
 ************************************************/
/* AFC Mock Inputs */
extern t_uint32            VaAPI_Cmp_NVMRegion[NVM_ARRAY_SIZE];
extern t_uint32            VeAPI_n_NVMRegionSize;
extern t_uint8            VaAPI_Cmp_NVMLoggingRegion[NVM_LOG_SIZE];
extern t_uint32            VeAPI_n_NVMLoggingRegion;
extern t_Pct_percent       VeAPI_Pct_PackSOC;
extern t_bool              VeAPI_b_PackSOC_DR;
extern t_I_milliamp        VeAPI_I_PackCurr;
extern t_bool              VeAPI_b_PackCurr_DR;
extern t_U_millivolt_cell  VaAPI_U_SEVolts[NUM_CELL_SERIES];
extern t_bool              VaAPI_b_SEVolts_DR[NUM_CELL_SERIES];
extern t_T_celsius         VaAPI_T_TempSnsrs[NUM_TEMP_SNSRS];
extern t_bool              VaAPI_b_TempSnsrs_DR[NUM_TEMP_SNSRS];
extern t_T_celsius         VeAPI_T_MinTempSnsr;
extern t_bool              VeAPI_b_MinTempSnsr_DR;
extern t_T_celsius         VeAPI_T_MaxTempSnsr;
extern t_bool              VeAPI_b_MaxTempSnsr_DR;
extern t_Cap_milliamphr    VeAPI_Cap_ChgPackCapcty;
extern t_bool              VeAPI_b_ChgPackCapcty_DR;
extern t_bool              VeAPI_b_EVSEChgStatus;
extern t_int32             VeAPI_e_EVSEChgLevel;
extern t_float32           VeAPI_e_Ab;
extern t_float32           VeAPI_e_Dp;
extern t_T_celsius         VeAPI_e_Tbgn;
extern t_T_celsius         VeAPI_e_Tlim;
extern t_float32           VeAPI_e_Alpha;
extern t_bool              VeAPI_e_NVMReset;
extern t_T_celsius         VeAPI_e_ChillerOnTemp;
extern t_uint32       VeAPI_e_TuningState;



extern struct AFC_Inputs_t AFC_Inputs;

/* AFC Mock Outputs */
extern t_uint8			   VaAFC_Cmp_AFC_to_CTE_Info[AFC_to_CTE_INFO_ARRAY_SIZE];
extern t_uint32            VeAFC_e_WarningFlags;
extern t_I_milliamp_chg    VeAFC_I_ChgPackCurr;
extern t_U_millivolt_pack  VeAFC_U_ChgPackVolt;
extern t_bool              VeAFC_b_ChgCompletionFlag;
extern t_bool              VeAFC_b_ExtremeAgingFlag;
extern t_bool              VeAFC_b_AbnormalAgingFlag;
extern t_bool              VeAFC_b_EarlyWarningAgingFlag;
extern t_bool              VeAFC_b_EOLFlag;
extern t_bool              VeAFC_b_SOCImbalanceFlag;




extern struct AFC_Outputs_t AFC_Outputs;

/* Obfuscation Variables */
extern t_int32 VeAPI_Cmp_LogSrc;
extern t_uint32 VeAPI_Cmp_LogSrcSize;
extern t_int32 VeAPI_Cmp_LogDst;

extern t_int32 VeAPI_Cmp_LogSrcArray[GENERIC_LOG_ARRAY_SIZE];
extern t_uint32 VeAPI_Cmp_LogSrcArraySize;
extern t_int32 VeAPI_Cmp_LogDstArray[GENERIC_LOG_ARRAY_SIZE];
extern t_U_millivolt_cell  cell_volts_temp[192];
extern LIB_CircBuffHandle_t Input_CircBuffHandle_t;
extern t_uint8*             ele_addr;



#else
#endif


#endif /* TEST_CONFIG_H_ */
