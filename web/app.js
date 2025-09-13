/**
 * @file app.js
 * @description App function for CS2 utility tools
 *
 * @author Awisuals
 * @created 2025-09-13
 * @updated 2025-09-13
 *
 * @module CS2_utility_tools
 * @see Related files or links
 *
 * @copyright © 2025 Awisuals
 * @license MIT
 */


// console.log("Hello world from app.js!")

export async function inLineSVG(url, container) {
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error('SVG fetch failed: ' + res.status);
        const svgText = await res.text();
        container.innerHTML = svgText; // Only for trusted SVGs
        container.querySelector('svg')?.setAttribute('role', 'img');
    } catch (error) {
        console.error(error);
        const img = document.createElement('img');
        img.src = url;
        img.alt = container.getAttribute('data-alt') || '';
        container.appendChild(img);
    }
}