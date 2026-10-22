// Node shim that shells out to the Python CLI and pipes JSON back.
const { spawnSync } = require("child_process");

const cmd = process.argv[2] || "status";
const res = spawnSync("python", ["-m", "warzone_dlc_unlocker.handlers.cli", cmd], {
  encoding: "utf8",
});

if (res.error) {
  console.error("failed to spawn python:", res.error.message);
  process.exit(1);
}

try {
  const data = JSON.parse(res.stdout.trim());
  console.log(JSON.stringify(data, null, 2));
} catch (e) {
  console.error("bad output:", res.stdout, res.stderr);
  process.exit(2);
}