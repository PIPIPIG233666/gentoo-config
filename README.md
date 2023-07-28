# gentoo-config

## Things actually used

### etc/default/amdgpu-custom-states.card0
#### AMD GPU overclock profile for RX 6800 XT

### etc/kernel/cmdline
#### cmdline for sbctl bundle generation

### etc/portage/make.conf
#### goodies for system-wide compiler optimization for Gentoo Linux

### how to start libvirt daemons
```
doas systemctl enable --now virtlockd
doas systemctl enable --now virtnodedevd
doas systemctl enable --now virtstoraged
doas systemctl enable --now virtqemud
doas systemctl enable --now virtchd
doas systemctl enable --now virtproxyd
doas systemctl enable --now virtinterfaced
doas systemctl enable --now virtlogd
doas systemctl enable --now virtsecretd
doas systemctl enable --now virtnetworkd
doas systemctl enable --now virtnwfilterd
```

### etc/genkernel.conf
compiler: llvm-clang, fs: zfs, microcode: amd

### etc/kernels/kernel-config-*
kconfig for genkernel
