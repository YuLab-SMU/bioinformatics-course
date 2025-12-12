import os
import json

VIDEO_DIR = 'video'
OUTPUT_FILE = 'videos.json'
VIDEO_EXTENSIONS = ('.mp4', '.webm', '.ogg', '.mov', '.avi', '.mkv')

def generate_json():
    videos = []
    if not os.path.exists(VIDEO_DIR):
        print(f"Error: Directory '{VIDEO_DIR}' not found.")
        return

    for root, dirs, files in os.walk(VIDEO_DIR):
        for file in files:
            if file.lower().endswith(VIDEO_EXTENSIONS):
                # 构建相对路径，用于 web 访问
                # 注意：在 Windows 上 os.path.join 会使用反斜杠，Web 需要正斜杠
                relative_path = os.path.join(root, file).replace(os.sep, '/')
                
                videos.append({
                    'name': file,
                    'path': relative_path
                })
    
    # 按名称排序，方便查看
    videos.sort(key=lambda x: x['name'])

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully generated {OUTPUT_FILE} with {len(videos)} videos.")

if __name__ == '__main__':
    generate_json()
