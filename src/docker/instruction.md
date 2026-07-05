# Practice Generation Instruction

## Purpose
Use this file to generate and maintain the Docker practice structure in this folder.

## Practice folder rules
Each practice folder should follow this structure:

1. A folder named with a clear topic, such as `5.healthchecks-and-troubleshooting`
2. A `README.md` file containing the task-only structure
3. An optional `instruction.md` file only when the practice needs extra guidance
4. Any supporting files needed for the exercise, such as `docker-compose.yml`, `Dockerfile`, or sample code

## README format
Each practice `README.md` should use this format:

- Title
- Status section with `[ ] Not started` or `[x] Completed`
- A short list of tasks
- Practice steps written as task bullets
- A final section for notes, observations, or conclusions

## Generation guidance
- Keep the task content focused on one Docker concept at a time.
- Use the same structure as [4.networking/README.md](4.networking/README.md) for consistency.
- Leave the content as task prompts first; the learner can later fill in the details and mark the section complete.
- Keep the practice relevant to the concepts already covered in [../../Notes/Docker/README.md](../../Notes/Docker/README.md).

## Maintenance guidance
- Add new practice folders when a new topic is introduced.
- Update [README.md](README.md) to include the new practice task.
- Keep the folder names numbered in order so the roadmap stays easy to follow.
