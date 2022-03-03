import pymem
import pymem.process
import time
from threading import Thread
import pygame
import pygame
import win32api
import win32con
import win32gui
from ctypes import windll

import requests

url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(url).json()

cs_gamerules_data = int(response["netvars"]["cs_gamerules_data"])

m_ArmorValue = int(response["netvars"]["m_ArmorValue"])
m_Collision = int(response["netvars"]["m_Collision"])
m_CollisionGroup = int(response["netvars"]["m_CollisionGroup"])
m_Local = int(response["netvars"]["m_Local"])
m_MoveType = int(response["netvars"]["m_MoveType"])
m_OriginalOwnerXuidHigh = int(response["netvars"]["m_OriginalOwnerXuidHigh"])
m_OriginalOwnerXuidLow = int(response["netvars"]["m_OriginalOwnerXuidLow"])
m_SurvivalGameRuleDecisionTypes = int(response["netvars"]["m_SurvivalGameRuleDecisionTypes"])
m_SurvivalRules = int(response["netvars"]["m_SurvivalRules"])
m_aimPunchAngleVel = int(response["netvars"]["m_aimPunchAngleVel"])
m_aimPunchAngle = int(response["netvars"]["m_aimPunchAngle"])
m_angEyeAnglesX = int(response["netvars"]["m_angEyeAnglesX"])
m_angEyeAnglesY = int(response["netvars"]["m_angEyeAnglesY"])
m_bBombPlanted = int(response["netvars"]["m_bBombPlanted"])
m_bFreezePeriod = int(response["netvars"]["m_bFreezePeriod"])
m_bGunGameImmunity = int(response["netvars"]["m_bGunGameImmunity"])
m_bHasDefuser = int(response["netvars"]["m_bHasDefuser"])
m_bHasHelmet = int(response["netvars"]["m_bHasHelmet"])
m_bInReload = int(response["netvars"]["m_bInReload"])
m_bIsDefusing = int(response["netvars"]["m_bIsDefusing"])
m_bIsQueuedMatchmaking = int(response["netvars"]["m_bIsQueuedMatchmaking"])
m_bIsScoped = int(response["netvars"]["m_bIsScoped"])
m_bIsValveDS = int(response["netvars"]["m_bIsValveDS"])
m_bSpotted = int(response["netvars"]["m_bSpotted"])
m_bSpottedByMask = int(response["netvars"]["m_bSpottedByMask"])
m_bStartedArming = int(response["netvars"]["m_bStartedArming"])
m_bUseCustomAutoExposureMax = int(response["netvars"]["m_bUseCustomAutoExposureMax"])
m_bUseCustomAutoExposureMin = int(response["netvars"]["m_bUseCustomAutoExposureMin"])
m_bUseCustomBloomScale = int(response["netvars"]["m_bUseCustomBloomScale"])
m_clrRender = int(response["netvars"]["m_clrRender"])
m_dwBoneMatrix = int(response["netvars"]["m_dwBoneMatrix"])
m_fAccuracyPenalty = int(response["netvars"]["m_fAccuracyPenalty"])
m_fFlags = int(response["netvars"]["m_fFlags"])
m_flC4Blow = int(response["netvars"]["m_flC4Blow"])
m_flCustomAutoExposureMax = int(response["netvars"]["m_flCustomAutoExposureMax"])
m_flCustomAutoExposureMin = int(response["netvars"]["m_flCustomAutoExposureMin"])
m_flCustomBloomScale = int(response["netvars"]["m_flCustomBloomScale"])
m_flDefuseCountDown = int(response["netvars"]["m_flDefuseCountDown"])
m_flDefuseLength = int(response["netvars"]["m_flDefuseLength"])
m_flFallbackWear = int(response["netvars"]["m_flFallbackWear"])
m_flFlashDuration = int(response["netvars"]["m_flFlashDuration"])
m_flFlashMaxAlpha = int(response["netvars"]["m_flFlashMaxAlpha"])
m_flLastBoneSetupTime = int(response["netvars"]["m_flLastBoneSetupTime"])
m_flLowerBodyYawTarget = int(response["netvars"]["m_flLowerBodyYawTarget"])
m_flNextAttack = int(response["netvars"]["m_flNextAttack"])
m_flNextPrimaryAttack = int(response["netvars"]["m_flNextPrimaryAttack"])
m_flSimulationTime = int(response["netvars"]["m_flSimulationTime"])
m_flTimerLength = int(response["netvars"]["m_flTimerLength"])
m_hActiveWeapon = int(response["netvars"]["m_hActiveWeapon"])
m_hMyWeapons = int(response["netvars"]["m_hMyWeapons"])
m_hObserverTarget = int(response["netvars"]["m_hObserverTarget"])
m_hOwner = int(response["netvars"]["m_hOwner"])
m_hOwnerEntity = int(response["netvars"]["m_hOwnerEntity"])
m_iAccountID = int(response["netvars"]["m_iAccountID"])
m_iClip1 = int(response["netvars"]["m_iClip1"])
m_iCompetitiveRanking = int(response["netvars"]["m_iCompetitiveRanking"])
m_iCompetitiveWins = int(response["netvars"]["m_iCompetitiveWins"])
m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])
m_iEntityQuality = int(response["netvars"]["m_iEntityQuality"])
m_iFOV = int(response["netvars"]["m_iDefaultFOV"])
m_iFOVStart = int(response["netvars"]["m_iFOVStart"])
m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])
m_iHealth = int(response["netvars"]["m_iHealth"])
m_iItemDefinitionIndex = int(response["netvars"]["m_iItemDefinitionIndex"])
m_iItemIDHigh = int(response["netvars"]["m_iItemIDHigh"])
m_iMostRecentModelBoneCounter = int(response["netvars"]["m_iMostRecentModelBoneCounter"])
m_iObserverMode = int(response["netvars"]["m_iObserverMode"])
m_iShotsFired = int(response["netvars"]["m_iShotsFired"])
m_iState = int(response["netvars"]["m_iState"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
m_lifeState = int(response["netvars"]["m_lifeState"])
m_nFallbackPaintKit = int(response["netvars"]["m_nFallbackPaintKit"])
m_nFallbackSeed = int(response["netvars"]["m_nFallbackSeed"])
m_nFallbackStatTrak = int(response["netvars"]["m_nFallbackStatTrak"])
m_nForceBone = int(response["netvars"]["m_nForceBone"])
m_nTickBase = int(response["netvars"]["m_nTickBase"])
m_rgflCoordinateFrame = int(response["netvars"]["m_rgflCoordinateFrame"])
m_szCustomName = int(response["netvars"]["m_szCustomName"])
m_szLastPlaceName = int(response["netvars"]["m_szLastPlaceName"])
m_thirdPersonViewAngles = int(response["netvars"]["m_thirdPersonViewAngles"])
m_vecOrigin = int(response["netvars"]["m_vecOrigin"])
m_vecVelocity = int(response["netvars"]["m_vecVelocity"])
m_vecViewOffset = int(response["netvars"]["m_vecViewOffset"])
m_viewPunchAngle = int(response["netvars"]["m_viewPunchAngle"])

anim_overlays = int(response["signatures"]["anim_overlays"])
clientstate_choked_commands = int(response["signatures"]["clientstate_choked_commands"])
clientstate_delta_ticks = int(response["signatures"]["clientstate_delta_ticks"])
clientstate_last_outgoing_command = int(response["signatures"]["clientstate_last_outgoing_command"])
clientstate_net_channel = int(response["signatures"]["clientstate_net_channel"])
convar_name_hash_table = int(response["signatures"]["convar_name_hash_table"])
dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
dwClientState = int(response["signatures"]["dwClientState"])
dwClientState_GetLocalPlayer = int(response["signatures"]["dwClientState_GetLocalPlayer"])
dwClientState_IsHLTV = int(response["signatures"]["dwClientState_IsHLTV"])
dwClientState_Map = int(response["signatures"]["dwClientState_Map"])
dwClientState_MapDirectory = int(response["signatures"]["dwClientState_MapDirectory"])
dwClientState_MaxPlayer = int(response["signatures"]["dwClientState_MaxPlayer"])
dwClientState_PlayerInfo = int(response["signatures"]["dwClientState_PlayerInfo"])
dwClientState_State = int(response["signatures"]["dwClientState_State"])
dwClientState_ViewAngles = int(response["signatures"]["dwClientState_ViewAngles"])
dwEntityList = int(response["signatures"]["dwEntityList"])
dwForceAttack = int(response["signatures"]["dwForceAttack"])
dwForceAttack2 = int(response["signatures"]["dwForceAttack2"])
dwForceBackward = int(response["signatures"]["dwForceBackward"])
dwForceForward = int(response["signatures"]["dwForceForward"])
dwForceJump = int(response["signatures"]["dwForceJump"])
dwForceLeft = int(response["signatures"]["dwForceLeft"])
dwForceRight = int(response["signatures"]["dwForceRight"])
dwGameDir = int(response["signatures"]["dwGameDir"])
dwGameRulesProxy = int(response["signatures"]["dwGameRulesProxy"])
dwGetAllClasses = int(response["signatures"]["dwGetAllClasses"])
dwGlobalVars = int(response["signatures"]["dwGlobalVars"])
dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])
dwInput = int(response["signatures"]["dwInput"])
dwInterfaceLinkList = int(response["signatures"]["dwInterfaceLinkList"])
dwMouseEnable = int(response["signatures"]["dwMouseEnable"])
dwMouseEnablePtr = int(response["signatures"]["dwMouseEnablePtr"])
dwPlayerResource = int(response["signatures"]["dwPlayerResource"])
dwSensitivity = int(response["signatures"]["dwSensitivity"])
dwSensitivityPtr = int(response["signatures"]["dwSensitivityPtr"])
dwRadarBase = int(response["signatures"]["dwRadarBase"])
dwSetClanTag = int(response["signatures"]["dwSetClanTag"])
dwViewMatrix = int(response["signatures"]["dwViewMatrix"])
dwWeaponTable = int(response["signatures"]["dwWeaponTable"])
dwWeaponTableIndex = int(response["signatures"]["dwWeaponTableIndex"])
dwYawPtr = int(response["signatures"]["dwYawPtr"])
dwZoomSensitivityRatioPtr = int(response["signatures"]["dwZoomSensitivityRatioPtr"])
dwbSendPackets = int(response["signatures"]["dwbSendPackets"])
dwppDirect3DDevice9 = int(response["signatures"]["dwppDirect3DDevice9"])
find_hud_element = int(response["signatures"]["find_hud_element"])
force_update_spectator_glow = int(response["signatures"]["force_update_spectator_glow"])
interface_engine_cvar = int(response["signatures"]["interface_engine_cvar"])
is_c4_owner = int(response["signatures"]["is_c4_owner"])
m_bDormant = int(response["signatures"]["m_bDormant"])
m_flSpawnTime = int(response["signatures"]["m_flSpawnTime"])
m_pStudioHdr = int(response["signatures"]["m_pStudioHdr"])
m_pitchClassPtr = int(response["signatures"]["m_pitchClassPtr"])
m_yawClassPtr = int(response["signatures"]["m_yawClassPtr"])
model_ambient_min = int(response["signatures"]["model_ambient_min"])
set_abs_angles = int(response["signatures"]["set_abs_angles"])
set_abs_origin = int(response["signatures"]["set_abs_origin"])

pm = pymem.Pymem("csgo.exe")
Client = pymem.process.module_from_name(pm.process_handle, 'client.dll').lpBaseOfDll

Width = win32api.GetSystemMetrics(0)
Height = win32api.GetSystemMetrics(1)

def W2S(posX, posY, posZ, view):
    clipCoordsX = posX * view[0] + posY * view[1] + posZ * view[2] + view[3]
    clipCoordsY = posX * view[4] + posY * view[5] + posZ * view[6] + view[7]
    clipCoordsZ = posX * view[8] + posY * view[9] + posZ * view[10] + view[11]
    clipCoordsW = posX * view[12] + posY * view[13] + posZ * view[14] + view[15]

    if clipCoordsW < 0.1:
        return False, 0, 0

    NDCx = clipCoordsX / clipCoordsW
    NDCy = clipCoordsY / clipCoordsW
    NDCz = clipCoordsZ / clipCoordsW

    screenX = (Width / 2 * NDCx) + (NDCx + Width / 2)
    screenY = -(Height / 2 * NDCy) + (NDCy + Height / 2)
    return True, screenX, screenY


def get_distance(PlAddr, EnAddr):
    enemy_posRx = pm.read_float(EnAddr + m_vecOrigin)
    enemy_posRy = pm.read_float(EnAddr + m_vecOrigin + 4)
    enemy_posRz = pm.read_float(EnAddr + m_vecOrigin + 8)

    my_posRx = pm.read_float(PlAddr + m_vecOrigin)
    my_posRy = pm.read_float(PlAddr + m_vecOrigin + 4)
    my_posRz = pm.read_float(PlAddr + m_vecOrigin + 8)

    my_posx = my_posX - enemy_posX
    my_posy = my_posY - enemy_posY
    my_posz = my_posZ - enemy_posZ

    return ((my_posx * my_posx + my_posy * my_posy + my_posz + my_posz) ** 0.5) / 10


def get_originpos(EnAddr):
    my_posRx = pm.read_float(EnAddr + m_vecOrigin)
    my_posRy = pm.read_float(EnAddr + m_vecOrigin + 4)
    my_posRz = pm.read_float(EnAddr + m_vecOrigin + 8)

    return my_posRx, my_posRy, my_posRz


def get_bonepos(Entity, n):
    Bonebase = pm.read_int(Entity + m_dwBoneMatrix)

    EnemyBonesx = pm.read_float(Bonebase + 0x30 * n + 0x0C)
    EnemyBonesy = pm.read_float(Bonebase + 0x30 * n + 0x1C)
    EnemyBonesz = pm.read_float(Bonebase + 0x30 * n + 0x2C)
    return EnemyBonesx, EnemyBonesy, EnemyBonesz


EntityList = {}


def FindEnt():
    global EntityList
    while 1:
        LocalPlayer = pm.read_int(Client + dwLocalPlayer)
        LocalTeam = pm.read_int(m_iTeamNum + LocalPlayer)
        TempEntityList = {}
        size = 0x174
        Struck = pm.read_int(Client + dwRadarBase)
        Pointer = pm.read_int(Struck + 0x78)
        for i in range(33):

            Entity = pm.read_int(Client + dwEntityList + (i * 0x10))
            PlNameI = i - 2
            name = pm.read_string((Pointer + 0x5E8) + (PlNameI * size))

            if (Entity and Entity != LocalPlayer):
                EntityDormsnt = pm.read_int(Entity + 0xED)
                if not EntityDormsnt:
                    TempEntityList[Entity] = name

        EntityList = TempEntityList
        time.sleep(1)


Thread(target=FindEnt).start()

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("HACK")
SetWindowPos = windll.user32.SetWindowPos
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()  # clock
alpha = 128
FPS = 60

bg_color = (0, 0, 0)
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*bg_color), 0, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0,
win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
red = (255, 0, 0)



while 1:
    clock.tick(FPS)

    screen.fill(bg_color)
    screen.set_alpha(128)
    TempEntityList = EntityList

    view = []
    for i in range(17):
        view.append(pm.read_float(Client + dwViewMatrix + (i * 4)))

    for Entity in TempEntityList:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        Hp = pm.read_int(Entity + 0x100)
        if not Hp: continue

        my_posRx, my_posRy, my_posRz = get_originpos(Entity)
        state, LegX, LegY = W2S(my_posRx, my_posRy, my_posRz, view)

        my_hedRx, my_hedRy, my_hedRz = get_bonepos(Entity, 8)
        state2, HeadX, HeadY = W2S(my_hedRx, my_hedRy, my_hedRz, view)

        if state and state2:
            Diff = HeadY - LegY
            HeadY += Diff // 5
            Diff = HeadY - LegY
            pygame.draw.line(screen, red, (LegX - Diff // 4, HeadY), (LegX - Diff // 4, LegY))
            pygame.draw.line(screen, red, (LegX + Diff // 4, HeadY), (LegX + Diff // 4, LegY))
            pygame.draw.line(screen, red, (LegX - Diff // 4, HeadY), (LegX + Diff // 4, HeadY))
            pygame.draw.line(screen, red, (LegX - Diff // 4, LegY), (LegX + Diff // 4, LegY))
    pygame.display.flip()
