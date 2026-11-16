---
tags:
  - linux
  - audio
  - fix
---
-: i am using cachy os my headphone is connected but i can't recive sound to it

![[Pasted image 20261114225845.png]]
![[Pasted image 20261114225907.png]]

Your WH-1000XM5 headphones are connected to Bluetooth, but the underlying audio system (PipeWire) has failed to register them as an available audio output.

Try these methods in order, checking your audio menu after each one.

### 1. Restart the Audio Services

Sometimes the audio services get out of sync and just need a quick refresh to detect connected Bluetooth devices.

1. Open your terminal.
    
2. Run the following command:
    
    Bash
    
    ```
    systemctl --user restart pipewire pipewire-pulse wireplumber
    ```
    

_Verification:_ Click your audio volume icon again and check if the WH-1000XM5 appears under Output Devices.

### 2. Clear WirePlumber State Files

If restarting the services didn't work, WirePlumber (the audio session manager) might have a corrupted state file preventing it from routing the audio.

1. Open your terminal.
    
2. Run these commands to back up the old state files and restart the service:
    
    Bash
    
    ```
    mv ~/.local/state/wireplumber ~/.local/state/wireplumber.bak
    systemctl --user restart wireplumber
    ```
    

_Verification:_ Open the audio menu to see if the headphones are now listed.

### 3. Forget and Re-pair the Headset

Occasionally, a device connects successfully, but the specific high-quality audio profile (A2DP) fails to negotiate during the Bluetooth handshake.

1. Open your Bluetooth settings, disconnect the WH-1000XM5, and completely remove/forget it.
    
2. Put the headphones back into pairing mode (usually by holding the power button down for several seconds while turning them on).
    
3. Pair and connect them through the Bluetooth menu again._Verification:_ Check the audio volume menu to see if the headset is now recognized as an output device.


