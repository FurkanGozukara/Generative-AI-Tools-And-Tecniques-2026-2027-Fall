# Resolution and generation cost

The two warm runs in the lecture use the same fixed seed, original prompt, eight steps, CFG one, res_multistep and simple scheduler.

| Resolution | Total prompt time | Final sampling rate | Approximate seconds per step | Sampled device memory peak |
|---|---:|---:|---:|---:|
| 512 × 512 | 0.972 s | 11.00 iterations/s | 0.091 s | 20.87 GiB |
| 1024 × 1024 | 3.225 s | 2.79 iterations/s | 0.358 s | 20.99 GiB |

The total is the backend execution interval. The reciprocal of the progress rate estimates seconds per sampling step; it is not the total divided by the step count. Initial model loading, prompt encoding, decoding and saving are separate work.

Device memory was sampled approximately every 0.2 seconds. It includes resident models and other allocations and may miss the instantaneous maximum. These warm totals do not isolate latent memory.

## Separate measurements of individual stages

These additional warm benchmark runs measure node transitions over the local WebSocket. Their timings include small event-delivery and scheduling effects; they are separate executions from the two console lines shown in the lecture.

| Resolution | Sampling node | Decode node | Observed job interval |
|---|---:|---:|---:|
| 512 × 512 | 0.969 s | 0.141 s | 1.375 s |
| 1024 × 1024 | 2.750 s | 0.203 s | 3.610 s |

The runtime that produced these numbers is listed at the end of the companion README. Doubling both image dimensions creates four times as many spatial positions; the implementation, attention, memory management and fixed overheads determine the measured runtime.
