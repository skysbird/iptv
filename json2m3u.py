import json

def json_to_m3u(json_path, output_path):
    with open(json_path, "r", encoding="utf-8") as f:
        channels = json.load(f)

    m3u_lines = ['#EXTM3U']

    for channel in channels:
        name = channel.get("name", "Unknown")
        language = channel.get("language", "")
        country = channel.get("country", "")
        geo_blocked = "yes" if channel.get("isGeoBlocked", False) else "no"
        group_title = country.upper() if country else "Other"

        # 构建 #EXTINF 行
        extinf = (
            f'#EXTINF:-1 '
            f'tvg-language="{language}" '
            f'group-title="{group_title}" '
            f'geo-blocked="{geo_blocked}",'
            f'{name}'
        )

        for url in channel.get("iptv_urls", []):
            m3u_lines.append(extinf)
            m3u_lines.append(url)
        
        for url in channel.get("youtube_urls", []):
            m3u_lines.append(extinf)
            m3u_lines.append(url)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(m3u_lines))

    print(f"✅ M3U 文件已保存至: {output_path}")


