<script lang="ts">
  import { onMount } from "svelte";
  import Tool from "./Tool.svelte";

  let typeFilter: string = "";
  let searchTerm: string = "";

  let tools: iTool[] = [];

  let limit = 25;
  let skip = 0;

  let loading = false;
  const getTools = async () => {
    const response = await fetch(
      `/api/tools?skip=${skip}&limit=${limit}&type=${typeFilter?.toUpperCase()}&search=${searchTerm}`,
    );
    const data = await response.json();
    tools = data;
  };

  onMount(async () => {
    loading = true;
    getTools().finally(() => (loading = false));
  });
</script>

<div class="">
  <div class="pb-4 border-b flex flex-wrap md:flex-row justify-between items-center">
    <form class="flex gap-4 items-end" on:submit={(e) => e.preventDefault()}>
      <label class="flex flex-col">
        Search
        <input
          type="text"
          placeholder="Search"
          class="border px-2 py-1"
          bind:value={searchTerm}
        />
      </label>
      <button
        class="border px-2 py-1 hover:bg-sky-100"
        type="submit"
        on:click={getTools}>Search</button
      >
    </form>
    <div class="flex gap-4">
      <div class="flex flex-col">
        <label for="limit"> Tools per page </label>
        <select
          name="limit"
          id="limit"
          bind:value={limit}
          on:change={getTools}
          class="border px-2 py-1"
        >
          <option disabled>Limit</option>
          <option value={25}>25</option>
          <option value={50}>50</option>
          <option value={100}>100</option>
        </select>
      </div>
      <label class="flex flex-col">
        Tool type
        <select
          name="type"
          id="type"
          on:change={(e) => {
            typeFilter = e.currentTarget.value;
            getTools();
          }}
          class="border px-2 py-1"
        >
          <option disabled>Type</option>
          <option value="">All</option>
          {#each ["Read", "Github Repo", "Website", "Sponsor"] as type}
            <option value={type}>{type}</option>
          {/each}
        </select>
      </label>
    </div>
  </div>
  {#if !loading}
    <ul>
      {#if tools.length == 0}
        <li class="text-center text-lg mt-8">No tools found</li>
      {/if}
      {#each tools as tool}
        <Tool {tool} />
      {/each}
    </ul>
    <div class="flex justify-center items-center gap-4 mt-4">
      <button
        class="border px-4 py-2 flex justify-center items-center rounded hover:bg-black/5"
        on:click={() => {
          if (skip > 0) {
            skip -= limit;
            getTools();
          }
        }}>{"<"}</button
      >
      <span>{skip + 1} - {skip + limit}</span>
      <button
        class="border px-4 py-2 flex justify-center items-center rounded hover:bg-black/5"
        on:click={() => {
          skip += limit;
          getTools();
        }}>{">"}</button
      >
    </div>
  {/if}
</div>
