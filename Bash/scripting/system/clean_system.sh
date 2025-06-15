#!/bin/bash

# ============================
# System Cleaning Script for Xubuntu
# Author: Anthony
# ============================

echo "🧹 Starting system cleanup..."

# Clean APT cache
echo "🧼 Cleaning APT cache..."
sudo apt clean
sudo apt autoclean
sudo apt autoremove -y

# Remove system temporary files
echo "🗑️ Removing temporary files from /tmp and /var/tmp..."
sudo rm -rf /tmp/*
sudo rm -rf /var/tmp/*

# Clear user cache
echo "📁 Deleting user cache (~/.cache)..."
rm -rf ~/.cache/*

# Remove thumbnails
echo "🖼️ Deleting thumbnail cache..."
rm -rf ~/.thumbnails/*
rm -rf ~/.cache/thumbnails/*

# Done
echo "✅ System cleanup completed successfully."
