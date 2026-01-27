/* ===================================================================
   This is an isolated_header file, it is solely for testing purposes.
   Expose definitions, functions, and variables that is normally private
   to the translation units for cffi cdef + pytest.

   WARNING: This header file is not intended for inclusion in any compilation units.
   =================================================================== */

#ifndef TEST_HARNESS_H_
#define TEST_HARNESS_H_

#pragma message ("Warning: You are including an isolated header file intended only for test extraction purposes.")

/************************************************
 * Expose Function Prototypes
 ************************************************/
void 				AFC_SetupStageParam(void);
t_I_milliamp_chg 	AFC_ChgCurrPresentStage(t_uint8 Le_i_PresentStageIdx);
t_uint8 			AFC_HighestCPVStageIdx(void);
t_uint8 			AFC_AttemptIncrementCPVIdx(t_uint8 Le_i_CPV_PresentIndex);
t_U_millivolt_cell 	AFC_CompensatedVoltage(t_U_millivolt_cell Le_U_SEVolt,
                                           t_U_millivolt_cell Le_U_CellOCV,
                                           t_float32 Le_r_TemperatureRatio,
                                           t_float32 Le_r_CurrRatio);
t_I_milliamp_chg 	AFC_ColdTempCompensation(t_I_milliamp_chg Le_I_ChgCurr, t_T_celsius Le_T_TempSnsr);
t_float32 			AFC_CalcCurrRatio(void);
t_float32 			AFC_CalcTemperatureRatio(t_T_celsius Le_T_TempSnsr);
t_U_millivolt_cell 	AFC_SOCtoOCV(t_Pct_percent Le_Pct_SOC);
void 				AFC_LoadNVM(t_uint8 Le_Cnt_StageNum);
void 				AFC_SaveNVM(t_uint8 Le_Cnt_StageNum);
void 				AFC_CPVTrack(void);
void                AFC_KeepTrackOfChrgCycles(t_Pct_percent Le_Pct_SOC);
void AFC_LogCorrIdxEvent( t_U_millivolt_cell  series_elements_val[]);


/************************************************
 * Exposed Struct Definitions
 ************************************************/
struct AFC_Param_VoltageImbalance_t {
	t_uint8 Ke_Cmp_SigmaLevel;
	t_U_millivolt_cell Ke_Cmp_NoiseFloor;
	t_time Ke_t_MinSamplingTime;
	t_uint8 Ke_Cnt_ThresholdForValidSample;
};

struct AFC_HighTempDerateAndTuningParameters_t {
	t_T_celsius Ke_k_BeginTemp;
	t_T_celsius Ke_k_DerateLimTemp;
	t_float32 Ke_k_Abruptness;
	t_float32 Ke_k_Dispersity;
    t_float32 Ke_k_Alpha;
    TuningState_t  Ke_e_TuningState;
};

/************************************************
 * Exposed Struct Declarations
 ************************************************/


/************************************************
 * Exposed Global Variables
 ************************************************/
extern t_uint8            QnovoAFC_LogVar2;
extern t_uint8            QnovoAFC_LogVar3[NUM_CELL_SERIES];
extern t_uint8            QnovoAFC_LogVar4;
extern t_uint8            QnovoAFC_LogVar5;
extern t_uint8            QnovoAFC_LogVar6;
extern t_float32          QnovoAFC_LogVar7;
extern t_uint8            QnovoAFC_LogVar8;
extern t_uint8            QnovoAFC_LogVar9[NUM_CELL_SERIES];
extern t_uint32			  QnovoAFC_LogVar10;
extern t_uint32			  QnovoAFC_LogVar11;
extern t_uint32			  QnovoAFC_LogVar12;
extern t_uint32			  QnovoAFC_LogVar13;
extern t_uint16			  QnovoAFC_LogVar14[NUM_CELL_SERIES];
extern t_uint16			  QnovoAFC_LogVar15[NUM_CELL_SERIES];
extern t_uint16			  QnovoAFC_LogVar16[NUM_CELL_SERIES];
extern t_float32          QnovoAFC_Log_VoltageImbalance_ZScore[NUM_CELL_SERIES];
extern t_float32          QnovoAFC_Log_VoltageImbalance_Threshold;

extern t_bool VeAFC_b_ControllerWakeUp;
extern t_bool VeAFC_b_Initialized;
extern t_float32 VaAFC_r_C_rate[AFC_NUM_TOTAL_STAGES];
extern t_Pct_percent KeAFC_Pct_TunableEndSOC;
extern t_Pct_percent Le_Pct_Previous_SOC;

/* Voltage Imbalance */
extern struct AFC_Param_VoltageImbalance_t AFC_Param_VoltageImbalance;
extern struct AFC_HighTempDerateAndTuningParameters_t AFC_HiTempDerate;



#endif // TEST_HARNESS_H_
