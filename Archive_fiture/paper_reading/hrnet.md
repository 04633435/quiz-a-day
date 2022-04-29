## title
    High-Resolution Representation Learinig for Human Pose Estimation

## topic
    Representation Learning

## contributions
    A new architecture that can maintain the high-resolution representation in the whole process keep the spatial information in a image. As a result, many cv tasks (region level or pixel level) can benifit from this maintenance of spatial information.
    
## proposed method/model/dataset/algorithm
    - A new architecture called HRnet
    - parallel multi-resolution subnetworks
    - repeated multi-scale fusion (exchange blocks, excahnge unit)

## results
    Compared to other SOTA methods based on the well-organized benchmarks.
    Benchmarks:
      - COCO benchmark:
        metrics used:
          - AP@0.5
          - AR
        result:
          - COCO Validation set
            | Method | Backbone | Pretrain | Input size | #Params | GFLOPs | AP AP^50 AP^75 AP^M AP^L AR |
            | ------ | -------- | -------- | --------   | ----- - | ------ | --------------------------- |
            | HRNet-W32 | HRNet-W32 | Y | 384x288   | 28.5M | 16.0 | 75.8 90.6 82.7 71.9 82.8 81.0 |
            | HRNet-W48 | HRNet-W48 | Y | 384x288   | 63.6M | 32.9 | 75.3 90.8 82.9 71.3 83.4 81.2 |
          - COCO test-dev set
            | Method | Backbone | Pretrain | Input size | #Params | GFLOPs | AP AP^50 AP^75 AP^M AP^L AR |
            | ------ | -------- | -------- | --------   | ----- - | ------ | --------------------------- |
            | HRNet-W32 | HRNet-W32 | Y | 384x288   | 28.5M | 16.0 | 74.9 92.5 82.8 71.3 80.9 80.1 |
            | HRNet-W48 | HRNet-W48 | Y | 384x288   | 63.6M | 32.9 | 75.5 92.7 84.5 73.4 83.1 82.0 |
            | HRNet-W48 + extra data | HRNet-W48 | Y | 384x288   | 63.6M | 32.9 | 77.0 92.7 84.5 73.4 83.1 82.0 |
      - MPII benchmark:
        metrics used:
          - PCKh@0.5
        result:
          surrpass almost all of SOTA mtthods, except for the method proposed by "Deeply learned compositional models for HPE".
          - MPII test set
            | Method | Hea Sho ELb Wri Hip Kne Ank | Total |
            | HRNet-W32 | 98.6 96.9 92.8 89.0 91.5 89.0 85.7 | 92.3 |

## conclusion
    - Conclusion
      - HRnet is a novel architecture that can maintain the spatial information, compared to other high2low-low2high architecture. And the results show that it did improve the performance on the task. This success comes from two aspect:
        - 1. maintain the high resolution through the whole process without the need of recovering the high resoltion
        - 2. fuse multi-resolution representations repeaedly, rendering reliable high-resolution representations
    - Further work
      - apply this work to other tasks, like face alignment, segmentation
      - implement the fuse operation in a light way