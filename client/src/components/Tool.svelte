<script lang="ts">
  export let tool: iTool;

  const getSpanColor = (type: string) => {
    switch (type) {
      case "READ":
        return "bg-green-300";
      case "GITHUB REPO":
        return "bg-blue-300";
      case "WEBSITE":
        return "bg-green-300";
      case "SPONSOR":
        return "bg-yellow-200";
      default:
        return "bg-red-300";
    }
  };
</script>

<div class="py-4 border-b">
  <div class="flex w-full">
    <div class="flex flex-col w-full">
      <div class="flex justify-between pb-4">
        <h3 class="text-xl">{tool.title}</h3>
        <span
          class={"rounded-full w-[15ch] justify-center flex px-2 py-1 h-max " +
            getSpanColor(tool.type)}>{tool.type}</span
        >
      </div>
      <p>{tool.description}</p>
      <a class="text-sky-600 underline" href={tool.url} target="_blank"
        >{tool.url.slice(0, 75)}{tool.url.length > 75 ? "..." : ""}</a
      >
    </div>
  </div>
</div>

<style>
  .link {
    max-width: 100ch;
  }
</style>
