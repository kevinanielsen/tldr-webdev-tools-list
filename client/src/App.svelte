<script lang="ts">
  import ToolsList from "./components/ToolsList.svelte";
</script>

<main class="p-4 flex flex-col items-center w-full h-full overflow-x-hidden overflow-y-auto">
  <div id="top"></div>
  <div
    class="h-16 top-0 p-4 border-b flex justify-between items-center fixed z-10 bg-white w-full"
  >
    <h1 class="sm:text-3xl text-xl" id="title">TLDR <span class="hidden sm:inline">Web Dev Tools</span></h1>
    <a
      href="https://refer.tldr.tech/1351f191/3"
      target="_blank"
      class="bg-sky-600 text-white px-2 py-1 rounded-full">Check out TLDR</a
    >
  </div>
  <div class="w-full max-w-4xl xl:border xl:border-y-0 md:p-8 mt-16">
    <ToolsList />
  </div>
  <button
    on:click={() =>
      document.querySelector("#top")?.scrollIntoView({
        behavior: "smooth",
      })}
    class="fixed bottom-0 right-0 m-4 rounded-full border flex justify-center items-center bg-white"
    ><img src="/chevron-up.svg" alt="Scroll to top" /></button
  >
</main>

<style>
</style>
