package com.entry.repository.mysql;

import com.entry.entity.mysql.Task;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface TaskRepository extends JpaRepository<Task, Integer> {

    @Query(value = "select * from task where id = ?1", nativeQuery = true)
    public Task findTaskById(Integer id);


}
