#!/bin/bash
# setup_networking.sh - Configure host NAT and bridges

BRIDGE_NAME="br-sandbox"
HOST_IFACE="eth0" # Change to your host's internet-facing interface

echo "[+] Creating bridge $BRIDGE_NAME..."
sudo ip link add name $BRIDGE_NAME type bridge
sudo ip link set $BRIDGE_NAME up
sudo ip addr add 192.168.100.1/24 dev $BRIDGE_NAME

echo "[+] Enabling IP forwarding and NAT..."
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o $HOST_IFACE -j MASQUERADE
sudo iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i $BRIDGE_NAME -o $HOST_IFACE -j ACCEPT
