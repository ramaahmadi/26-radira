#!/usr/bin/env python3
"""
Album 26 Cover Generator
Creates an album cover artwork representing the journey of growth and resilience.
The cover visualizes the 5 chapters of transformation described in the album story.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import matplotlib.patheffects as path_effects
from PIL import Image, ImageDraw, ImageFont
import io

def create_catchy_album_cover():
    """
    Create a modern, eye-catching album cover with vibrant colors and bold design
    """
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    fig.patch.set_facecolor('#000000')
    ax.set_facecolor('#000000')
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Create vibrant gradient background with neon colors
    x = np.linspace(0, 12, 300)
    y = np.linspace(0, 12, 300)
    X, Y = np.meshgrid(x, y)
    
    # Multi-color gradient for eye-catching effect
    R = np.sin(X/2) * np.cos(Y/2) * 0.5 + 0.5
    G = np.sin(X/3 + np.pi/3) * np.cos(Y/3 + np.pi/3) * 0.5 + 0.5
    B = np.sin(X/4 + 2*np.pi/3) * np.cos(Y/4 + 2*np.pi/3) * 0.5 + 0.5
    
    # Apply vibrant color map
    ax.imshow(R, extent=[0, 12, 0, 12], cmap='hot', alpha=0.3, aspect='auto')
    ax.imshow(G, extent=[0, 12, 0, 12], cmap='plasma', alpha=0.3, aspect='auto')
    ax.imshow(B, extent=[0, 12, 0, 12], cmap='viridis', alpha=0.3, aspect='auto')
    
    # Add geometric patterns for modern look
    # Hexagon pattern in background
    for i in range(0, 13, 2):
        for j in range(0, 13, 2):
            hexagon = patches.RegularPolygon((i, j), 6, radius=0.8, 
                                            facecolor='none', 
                                            edgecolor='#00ffff', 
                                            alpha=0.2, 
                                            linewidth=1)
            ax.add_patch(hexagon)
    
    # Central focal point - glowing orb
    for i in range(5, 0, -1):
        glow = patches.Circle((6, 6), i, 
                              color='#ff00ff', 
                              alpha=0.1 * (6-i), 
                              edgecolor='none')
        ax.add_patch(glow)
    
    # Dynamic journey path with neon effect
    t = np.linspace(0, 4*np.pi, 200)
    path_x = 6 + 4*np.cos(t) * np.exp(-t/10)
    path_y = 6 + 4*np.sin(t) * np.exp(-t/10)
    
    # Neon path effect with multiple layers
    for width, alpha in [(8, 0.1), (5, 0.2), (3, 0.4), (2, 0.8)]:
        ax.plot(path_x, path_y, color='#00ffff', linewidth=width, alpha=alpha)
    
    # Chapter representations with modern icons
    chapters = [
        {'pos': (3, 3), 'color': '#ff0066', 'symbol': '🌱', 'size': 0.8},
        {'pos': (9, 3), 'color': '#ffaa00', 'symbol': '⚡', 'size': 0.9},
        {'pos': (3, 9), 'color': '#00ff88', 'symbol': '🦋', 'size': 1.0},
        {'pos': (9, 9), 'color': '#00aaff', 'symbol': '🌟', 'size': 1.1},
        {'pos': (6, 6), 'color': '#ff00ff', 'symbol': '👤', 'size': 1.2}
    ]
    
    for chapter in chapters:
        # Glowing background circle
        for i in range(3, 0, -1):
            glow_circle = patches.Circle(chapter['pos'], chapter['size'] * (1 + i*0.3), 
                                         color=chapter['color'], 
                                         alpha=0.05, 
                                         edgecolor='none')
            ax.add_patch(glow_circle)
        
        # Main circle
        main_circle = patches.Circle(chapter['pos'], chapter['size'], 
                                    color=chapter['color'], 
                                    alpha=0.8, 
                                    edgecolor='white', 
                                    linewidth=2)
        ax.add_patch(main_circle)
    
    # Bold "26" in center with 3D effect
    for offset, color, alpha in [(0.15, '#000000', 0.8), (0.1, '#333333', 0.6), 
                                   (0.05, '#666666', 0.4), (0, '#ffffff', 1.0)]:
        ax.text(6 + offset, 6 - offset, '26', 
                fontsize=120, fontweight='bold', 
                color=color, alpha=alpha,
                ha='center', va='center',
                family='Arial Black')
    
    # Neon glow around "26"
    for i in range(3):
        glow_text = ax.text(6, 6, '26', 
                           fontsize=120 + i*10, fontweight='bold', 
                           color='#ff00ff', alpha=0.1,
                           ha='center', va='center',
                           family='Arial Black')
        glow_text.set_path_effects([path_effects.Stroke(linewidth=5+i*2, foreground='#00ffff')])
    
    # Add album title with modern typography
    ax.text(6, 1.5, 'STORIES OF RESILIENCE', 
            fontsize=18, fontweight='bold', color='white', 
            ha='center', va='center', alpha=0.9,
            family='Arial',
            path_effects=[path_effects.withStroke(linewidth=2, foreground='#ff00ff')])
    
    # Add decorative elements
    # Floating particles
    np.random.seed(42)
    for _ in range(50):
        x, y = np.random.uniform(0, 12, 2)
        size = np.random.uniform(0.05, 0.2)
        particle = patches.Circle((x, y), size, 
                                 color=np.random.choice(['#00ffff', '#ff00ff', '#ffff00', '#00ff00']), 
                                 alpha=np.random.uniform(0.3, 0.8))
        ax.add_patch(particle)
    
    # Lightning bolts for energy
    for _ in range(5):
        x_start, y_start = np.random.uniform(1, 11, 2)
        x_end, y_end = np.random.uniform(1, 11, 2)
        mid_x = (x_start + x_end) / 2 + np.random.uniform(-1, 1)
        mid_y = (y_start + y_end) / 2 + np.random.uniform(-1, 1)
        
        lightning_x = [x_start, mid_x, x_end]
        lightning_y = [y_start, mid_y, y_end]
        
        ax.plot(lightning_x, lightning_y, color='#ffff00', linewidth=2, alpha=0.6)
    
    plt.tight_layout()
    plt.savefig('/Users/ramaahmadi/Dokumen/Album/album_26_cover_catchy.png', 
                dpi=300, bbox_inches='tight', facecolor='#000000', 
                edgecolor='none', pad_inches=0.1)
    plt.close()
    
    print("✅ Eye-catching album cover created!")
    print("📍 Saved as: album_26_cover_catchy.png")
    print("🎨 Features: Neon effects, vibrant colors, modern design")

def create_album_cover():
    """
    Create album cover artwork for Album 26 - Stories of Resilience
    Visual representation of the 5 chapters of personal transformation
    """
    
    # Create figure with square aspect ratio for album cover
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    fig.patch.set_facecolor('#0a0a0a')
    ax.set_facecolor('#0a0a0a')
    
    # Remove axes for clean artwork
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Create gradient background representing the journey
    gradient = np.linspace(0, 1, 256).reshape(256, 1)
    gradient = np.hstack([gradient] * 256)
    
    # Dark to light gradient symbolizing growth
    extent = [0, 10, 0, 10]
    ax.imshow(gradient.T, extent=extent, aspect='auto', cmap='twilight', alpha=0.3)
    
    # Draw the journey path - curved line representing life's path
    journey_x = np.linspace(1, 9, 100)
    journey_y = 2 + 3*np.sin(journey_x * 0.8) + 0.5*journey_x
    ax.plot(journey_x, journey_y, color='white', linewidth=3, alpha=0.8, path_effects=[path_effects.withStroke(linewidth=5, foreground='#4a5568')])
    
    # Chapter 1: Grew Up Before Recess - Small figure at beginning
    chapter1_x, chapter1_y = 1.5, 2.5
    # Small child figure
    child_circle = patches.Circle((chapter1_x, chapter1_y), 0.3, color='#9ca3af', alpha=0.8)
    ax.add_patch(child_circle)
    # Small arms reaching up
    ax.plot([chapter1_x-0.2, chapter1_x+0.2], [chapter1_y+0.3, chapter1_y+0.3], color='#9ca3af', linewidth=2)
    # Storm cloud above - challenges
    storm_cloud = patches.Ellipse((chapter1_x, chapter1_y+1), 0.8, 0.3, color='#6b7280', alpha=0.4)
    ax.add_patch(storm_cloud)
    
    # Chapter 2: 26 - Middle point with reflection
    chapter2_x, chapter2_y = 5, 5.5
    # Figure looking in mirror
    figure_circle = patches.Circle((chapter2_x, chapter2_y), 0.4, color='#8b5cf6', alpha=0.8)
    ax.add_patch(figure_circle)
    # Mirror reflection
    mirror = patches.Rectangle((chapter2_x+0.8, chapter2_y-0.5), 0.1, 1, color='#e5e7eb', alpha=0.6)
    ax.add_patch(mirror)
    # Reflection figure
    reflection = patches.Circle((chapter2_x+1.2, chapter2_y), 0.35, color='#8b5cf6', alpha=0.3)
    ax.add_patch(reflection)
    
    # Chapter 3: Not That Boy - Breaking away
    chapter3_x, chapter3_y = 6.5, 4
    # Breaking chains
    chain1 = patches.Rectangle((chapter3_x-0.8, chapter3_y), 0.3, 0.05, color='#6b7280', alpha=0.6)
    chain2 = patches.Rectangle((chapter3_x-0.4, chapter3_y), 0.3, 0.05, color='#6b7280', alpha=0.6)
    chain3 = patches.Rectangle((chapter3_x, chapter3_y), 0.3, 0.05, color='#6b7280', alpha=0.3)  # Broken
    ax.add_patch(chain1)
    ax.add_patch(chain2)
    ax.add_patch(chain3)
    # Figure breaking free
    breaking_figure = patches.Circle((chapter3_x, chapter3_y+0.5), 0.45, color='#ec4899', alpha=0.8)
    ax.add_patch(breaking_figure)
    
    # Chapter 4: New Man, New Me - Transformation
    chapter4_x, chapter4_y = 7.5, 6
    # Butterfly transformation
    butterfly_body = patches.Ellipse((chapter4_x, chapter4_y), 0.1, 0.3, color='#22c55e', alpha=0.9)
    ax.add_patch(butterfly_body)
    # Wings
    left_wing = patches.Ellipse((chapter4_x-0.3, chapter4_y), 0.4, 0.2, angle=30, color='#22c55e', alpha=0.7)
    right_wing = patches.Ellipse((chapter4_x+0.3, chapter4_y), 0.4, 0.2, angle=-30, color='#22c55e', alpha=0.7)
    ax.add_patch(left_wing)
    ax.add_patch(right_wing)
    
    # Chapter 5: The Man I'm Trying to Be - Reaching potential
    chapter5_x, chapter5_y = 8.5, 7.5
    # Mature figure reaching upward
    mature_figure = patches.Circle((chapter5_x, chapter5_y), 0.5, color='#22c55e', alpha=0.8)
    ax.add_patch(mature_figure)
    # Arms reaching up
    ax.plot([chapter5_x-0.4, chapter5_x-0.2], [chapter5_y+0.4, chapter5_y+0.8], color='#22c55e', linewidth=3)
    ax.plot([chapter5_x+0.4, chapter5_x+0.2], [chapter5_y+0.4, chapter5_y+0.8], color='#22c55e', linewidth=3)
    # Star at the peak - achievement
    star_x, star_y = chapter5_x, chapter5_y + 1.2
    star = patches.Polygon([
        [star_x, star_y + 0.3], [star_x + 0.1, star_y + 0.1], 
        [star_x + 0.3, star_y + 0.1], [star_x + 0.15, star_y - 0.05],
        [star_x + 0.2, star_y - 0.2], [star_x, star_y - 0.1],
        [star_x - 0.2, star_y - 0.2], [star_x - 0.15, star_y - 0.05],
        [star_x - 0.3, star_y + 0.1], [star_x - 0.1, star_y + 0.1]
    ], color='#fbbf24', alpha=0.9)
    ax.add_patch(star)
    
    # Add stars along the journey - achievements and milestones
    star_positions = [(2.5, 3.5), (4, 4.8), (6, 5.2), (7.2, 6.8)]
    for star_x, star_y in star_positions:
        small_star = patches.Polygon([
            [star_x, star_y + 0.15], [star_x + 0.05, star_y + 0.05], 
            [star_x + 0.15, star_y + 0.05], [star_x + 0.075, star_y - 0.025],
            [star_x + 0.1, star_y - 0.1], [star_x, star_y - 0.05],
            [star_x - 0.1, star_y - 0.1], [star_x - 0.075, star_y - 0.025],
            [star_x - 0.15, star_y + 0.05], [star_x - 0.05, star_y + 0.05]
        ], color='#fbbf24', alpha=0.6)
        ax.add_patch(small_star)
    
    # Add the number "26" prominently
    ax.text(5, 1.5, '26', fontsize=48, fontweight='bold', color='white', 
            ha='center', va='center', alpha=0.9,
            path_effects=[path_effects.withStroke(linewidth=3, foreground='#8b5cf6')])
    
    # Add album title
    ax.text(5, 0.8, 'Stories of Resilience', fontsize=14, color='white', 
            ha='center', va='center', alpha=0.7, style='italic')
    
    # Add subtle grid pattern representing structure/growth
    for i in range(0, 11, 2):
        ax.axhline(y=i, color='white', alpha=0.05, linewidth=0.5)
        ax.axvline(x=i, color='white', alpha=0.05, linewidth=0.5)
    
    # Save the artwork
    plt.tight_layout()
    plt.savefig('/Users/ramaahmadi/Dokumen/Album/album_26_cover.png', 
                dpi=300, bbox_inches='tight', facecolor='#0a0a0a', 
                edgecolor='none', pad_inches=0.2)
    plt.close()
    
    print("✅ Album cover created successfully!")
    print("📍 Saved as: album_26_cover.png")
    print("🎨 Cover represents the 5 chapters of growth and resilience")

def create_alternative_cover():
    """
    Create an alternative minimalist cover design
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Create concentric circles representing growth stages
    circles = [
        {'center': (5, 5), 'radius': 4, 'color': '#0f3460', 'alpha': 0.3},
        {'center': (5, 5), 'radius': 3, 'color': '#16213e', 'alpha': 0.4},
        {'center': (5, 5), 'radius': 2, 'color': '#533483', 'alpha': 0.5},
        {'center': (5, 5), 'radius': 1, 'color': '#e94560', 'alpha': 0.6},
    ]
    
    for circle in circles:
        circle_patch = patches.Circle(circle['center'], circle['radius'], 
                                     color=circle['color'], alpha=circle['alpha'])
        ax.add_patch(circle_patch)
    
    # Add path through the circles
    theta = np.linspace(0, 4*np.pi, 200)
    r = np.linspace(0.5, 3.5, 200)
    x = 5 + r * np.cos(theta)
    y = 5 + r * np.sin(theta)
    ax.plot(x, y, color='white', linewidth=2, alpha=0.8)
    
    # Central figure
    central_figure = patches.Circle((5, 5), 0.3, color='white', alpha=0.9)
    ax.add_patch(central_figure)
    
    # Number 26
    ax.text(5, 5, '26', fontsize=36, fontweight='bold', color='white', 
            ha='center', va='center', alpha=0.9)
    
    # Save alternative cover
    plt.tight_layout()
    plt.savefig('/Users/ramaahmadi/Dokumen/Album/album_26_cover_alt.png', 
                dpi=300, bbox_inches='tight', facecolor='#1a1a2e')
    plt.close()
    
    print("✅ Alternative album cover created!")
    print("📍 Saved as: album_26_cover_alt.png")

def create_neon_cover():
    """
    Create a vibrant neon-style album cover with cyberpunk aesthetics
    """
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    fig.patch.set_facecolor('#0a0a0a')
    ax.set_facecolor('#0a0a0a')
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Create dark gradient background
    x = np.linspace(0, 12, 200)
    y = np.linspace(0, 12, 200)
    X, Y = np.meshgrid(x, y)
    Z = np.sqrt((X-6)**2 + (Y-6)**2)
    ax.imshow(Z, extent=[0, 12, 0, 12], cmap='magma', alpha=0.4, aspect='auto')
    
    # Add grid lines for tech feel
    for i in range(0, 13, 1):
        ax.axvline(x=i, color='#00ffff', alpha=0.1, linewidth=0.5)
        ax.axhline(y=i, color='#00ffff', alpha=0.1, linewidth=0.5)
    
    # Create neon "26" with multiple glow effects
    colors = ['#ff00ff', '#00ffff', '#ffff00', '#ff00aa', '#00ff00']
    for i, color in enumerate(colors):
        offset = i * 0.08
        alpha = 0.3 - i * 0.05
        ax.text(6 + offset, 6 - offset, '26', 
                fontsize=140 - i*10, fontweight='bold', 
                color=color, alpha=alpha,
                ha='center', va='center',
                family='Arial Black')
    
    # Main white "26"
    ax.text(6, 6, '26', 
            fontsize=100, fontweight='bold', 
            color='white', alpha=1.0,
            ha='center', va='center',
            family='Arial Black',
            path_effects=[path_effects.withStroke(linewidth=3, foreground='#ff00ff')])
    
    # Add neon circles around the number
    for i in range(3):
        radius = 3 + i * 0.5
        circle = patches.Circle((6, 6), radius, 
                              fill=False, 
                              edgecolor=['#00ffff', '#ff00ff', '#ffff00'][i], 
                              alpha=0.6 - i*0.2, 
                              linewidth=3-i)
        ax.add_patch(circle)
    
    # Add geometric shapes for modern look
    # Triangles
    triangle_positions = [(2, 2), (10, 2), (2, 10), (10, 10)]
    for pos in triangle_positions:
        triangle = patches.RegularPolygon(pos, 3, radius=0.8, 
                                        facecolor='none', 
                                        edgecolor='#00ff00', 
                                        alpha=0.6, 
                                        linewidth=2)
        ax.add_patch(triangle)
    
    # Add title with neon effect
    ax.text(6, 1.5, 'STORIES OF RESILIENCE', 
            fontsize=16, fontweight='bold', color='#00ffff', 
            ha='center', va='center', alpha=0.9,
            family='Arial',
            path_effects=[path_effects.withStroke(linewidth=2, foreground='#ff00ff')])
    
    # Add random neon dots for atmosphere
    np.random.seed(123)
    for _ in range(30):
        x, y = np.random.uniform(0, 12, 2)
        dot = patches.Circle((x, y), 0.1, 
                            color=np.random.choice(['#ff00ff', '#00ffff', '#ffff00']), 
                            alpha=np.random.uniform(0.5, 1.0))
        ax.add_patch(dot)
    
    plt.tight_layout()
    plt.savefig('/Users/ramaahmadi/Dokumen/Album/album_26_cover_neon.png', 
                dpi=300, bbox_inches='tight', facecolor='#0a0a0a', 
                edgecolor='none', pad_inches=0.1)
    plt.close()
    
    print("✅ Neon album cover created!")
    print("📍 Saved as: album_26_cover_neon.png")
    print("🎨 Features: Cyberpunk style, neon effects, tech aesthetic")

def create_gradient_cover():
    """
    Create a modern gradient cover with smooth color transitions
    """
    fig, ax = plt.subplots(1, 1, figsize=(12, 12))
    fig.patch.set_facecolor('#000000')
    ax.set_facecolor('#000000')
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Create beautiful gradient background
    x = np.linspace(0, 12, 300)
    y = np.linspace(0, 12, 300)
    X, Y = np.meshgrid(x, y)
    
    # Create radial gradient
    R = np.sqrt((X-6)**2 + (Y-6)**2)
    gradient = np.exp(-R/3) * np.sin(R/2) + 0.5
    
    # Apply multiple color maps for rich gradient
    ax.imshow(gradient, extent=[0, 12, 0, 12], cmap='twilight', alpha=0.8, aspect='auto')
    ax.imshow(gradient.T, extent=[0, 12, 0, 12], cmap='plasma', alpha=0.4, aspect='auto')
    
    # Add flowing waves for dynamic effect
    for i in range(5):
        t = np.linspace(0, 4*np.pi, 200)
        x_wave = 12 * t / (4*np.pi)
        y_wave = 6 + 2*np.sin(t + i*np.pi/3) * np.exp(-i*0.2)
        
        ax.plot(x_wave, y_wave, 
               color=['#ff0066', '#ffaa00', '#00ff88', '#00aaff', '#ff00ff'][i], 
               linewidth=3-i*0.4, alpha=0.7-i*0.1)
    
    # Create elegant "26" with gradient effect
    for i in range(10):
        offset = i * 0.02
        size = 80 - i * 2
        alpha = 0.1 + i * 0.08
        
        color = plt.cm.rainbow(i / 10)[:3]
        ax.text(6 + offset, 6 - offset, '26', 
                fontsize=size, fontweight='bold', 
                color=color, alpha=alpha,
                ha='center', va='center',
                family='Arial')
    
    # Main white "26" with shadow
    ax.text(6.05, 5.95, '26', 
            fontsize=70, fontweight='bold', 
            color='black', alpha=0.5,
            ha='center', va='center',
            family='Arial Black')
    
    ax.text(6, 6, '26', 
            fontsize=70, fontweight='bold', 
            color='white', alpha=1.0,
            ha='center', va='center',
            family='Arial Black')
    
    # Add decorative circles
    for i in range(8):
        angle = i * np.pi / 4
        x_pos = 6 + 4 * np.cos(angle)
        y_pos = 6 + 4 * np.sin(angle)
        
        circle = patches.Circle((x_pos, y_pos), 0.5, 
                              color=plt.cm.rainbow(i / 8)[:3], 
                              alpha=0.6)
        ax.add_patch(circle)
    
    # Add title
    ax.text(6, 1.5, 'Stories of Resilience', 
            fontsize=18, fontweight='300', color='white', 
            ha='center', va='center', alpha=0.9,
            family='Arial')
    
    plt.tight_layout()
    plt.savefig('/Users/ramaahmadi/Dokumen/Album/album_26_cover_gradient.png', 
                dpi=300, bbox_inches='tight', facecolor='#000000', 
                edgecolor='none', pad_inches=0.1)
    plt.close()
    
    print("✅ Gradient album cover created!")
    print("📍 Saved as: album_26_cover_gradient.png")
    print("🎨 Features: Smooth gradients, flowing waves, rainbow colors")

if __name__ == "__main__":
    print("🎵 Creating Eye-Catching Album 26 Cover Art...")
    print("📖 Story: 5 chapters of growth and resilience")
    print("🎨 Multiple modern designs for maximum visual impact")
    print("💫 Neon effects, gradients, and vibrant colors")
    print()
    
    # Original cover
    print("🔄 Creating original cover...")
    create_album_cover()
    print()
    
    # Alternative minimalist cover
    print("🔄 Creating alternative cover...")
    create_alternative_cover()
    print()
    
    # New eye-catching covers
    print("🔄 Creating catchy modern cover...")
    create_catchy_album_cover()
    print()
    
    print("🔄 Creating neon cyberpunk cover...")
    create_neon_cover()
    print()
    
    print("🔄 Creating gradient cover...")
    create_gradient_cover()
    print()
    
    print("🎉 All album covers ready!")
    print("📁 Original: album_26_cover.png")
    print("📁 Alternative: album_26_cover_alt.png")
    print("📁 Catchy Modern: album_26_cover_catchy.png")
    print("📁 Neon Cyberpunk: album_26_cover_neon.png")
    print("📁 Gradient Flow: album_26_cover_gradient.png")
    print()
    print("✨ All covers are high-resolution (300dpi) and ready for streaming platforms!")
