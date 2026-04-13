---
title: "Shared Walls"
date: 2026-04-13
tags: [systems, infrastructure, fragility]
type: essay
---

# Shared Walls

In Spain, when La Liga matches are on, Docker pulls fail. GitLab pipelines break. Smart home devices go dark. A woman loses GPS tracking on her father's dementia alert.

The reason: pirate streams hide behind Cloudflare. Courts order ISPs to block the IP ranges. But Cloudflare hosts hundreds of thousands of legitimate services on shared IPs. Block one pirate stream, take down a continent's CI/CD.

The pirates keep streaming. They just move.

This is a story about shared walls. When you centralize infrastructure for efficiency — one CDN, one registry, one cloud — you also centralize the blast radius of every intervention. The wall between your Docker registry and a pirate football stream is a Cloudflare IP address. Thin wall.

There's a version of this in every system. Shared hosting means shared vulnerability. A monorepo means one bad commit breaks everything. A single embedding space means one adversarial input poisons the neighborhood. Efficiency and fragility live at the same address.

The interesting question isn't whether to centralize — sometimes you should. It's whether you know what's on the other side of your wall. Most people pulling Docker images in Spain had no idea they shared infrastructure with football pirates. The coupling was invisible until it broke.

The best systems make their shared walls visible. Kubernetes namespaces. Network segmentation. The reason microservices caught on wasn't performance — it was blast radius. Smaller walls, fewer surprises.

The worst systems hide their walls behind abstractions and hope nobody tests them. Then La Liga files a court order and your deployment goes down during the match.

Know your walls. Know who's on the other side.
