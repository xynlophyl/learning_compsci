# learning:others
workspace for other concepts and ideas that I pick up on.

## Project Ideas
### SoccerTracking
- [SoccerNet Game State Reconstruction](https://arxiv.org/pdf/2404.11335)
- Extension Ideas
    - Position smoothing 
    - Background: object locations can be volatile since we are performing keypoint detection and perspective transformations for each frame to account for camera movements (this applies for all objects: ball, players) 
    - Solution: use neural net to predict the actual next location of object track 
    - Model Selection
      - LSTM model for time series predictions 
      - GNN to represent graphical nature of team formations 
      - RL agent to act as a reward-maximizer and find the best position to lead to a goal (could be a completely separate idea) 
    - Data: [SoccerNet](https://huggingface.co/datasets/SoccerNet/SN-GSR-2024/tree/main) (has ground truths to train model) 
    - Potential Issues: 
      - Configuring multimodal pipeline (keypoint -> perspective transform -> smoothing)
      - How to (or need to?) assign backprop to fine tune keypoint model
### MapReduce (CUDA)
- [MapReduce Paper](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
- [Numba CUDA tutorial](https://colab.research.google.com/github/NVIDIA/accelerated-computing-hub/blob/main/gpu-python-tutorial/2.0_Numba.ipynb?authuser=1#scrollTo=9723dc8a-9627-442f-becc-3d9fc5423096)
- [Numba tutorial 2](https://colab.research.google.com/github/NVIDIA/accelerated-computing-hub/blob/main/gpu-python-tutorial/3.0_Numba_gauss.ipynb#scrollTo=21fd0189-6e1a-49d1-972f-dc0e411548e4)

## Areas of Interest
[Algorithmic Game Theory](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf)
