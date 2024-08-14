import asyncio
import subprocess

class CodeExecutor:
    async def execute_python(self, code):
        process = await asyncio.create_subprocess_exec(
            'python', '-c', code,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {
            "output": stdout.decode(),
            "error": stderr.decode(),
            "return_code": process.returncode
        }

    async def execute_javascript(self, code):
        process = await asyncio.create_subprocess_exec(
            'node', '-e', code,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {
            "output": stdout.decode(),
            "error": stderr.decode(),
            "return_code": process.returncode
        }