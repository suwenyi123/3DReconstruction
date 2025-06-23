import os
import imageio

video_path = "/home/wenyisu/cvagent/step3/part3/train/1/data/cat2.mp4"
output_dir = "/home/wenyisu/cvagent/step3/part3/train/1/images"
os.makedirs(output_dir, exist_ok=True)

reader = imageio.get_reader(video_path)
save_every = 3  # 每隔多少帧保存一帧

saved = 0
for i, frame in enumerate(reader):
    if i % save_every == 0:
        frame_path = os.path.join(output_dir, f"frame_{saved:04d}.jpg")
        imageio.imwrite(frame_path, frame)
        print(f"Saved: {frame_path}")
        saved += 1

print(f" 共保存了 {saved} 张图像（每 {save_every} 帧保存一张）")
